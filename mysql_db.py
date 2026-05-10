# MySQL Database Functions

# Import MySQL connector package
import mysql.connector


# Create and return a MySQL database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="appdbproj"
    )


# Test MySQL database connection
def test_mysql_connection():
    try:
        conn = get_connection()
        conn.close()
        return True

    # Display connection error if connection fails
    except Exception as e:
        print("MySQL connection error:", e)
        return False


# Search for speakers and related session information
def search_speakers_sessions(search_text):
    conn = get_connection()
    cursor = conn.cursor()

    # SQL query to retrieve speaker, session, and room details
    query = """
        SELECT 
            session.speakerName,
            session.sessionTitle,
            room.roomName
        FROM session
        JOIN room ON session.roomID = room.roomID
        WHERE session.speakerName LIKE %s;
    """

    # Execute query using wildcard search
    cursor.execute(query, (f"%{search_text}%",))
    results = cursor.fetchall()

    conn.close()
    return results


# Retrieve company name using company ID
def get_company_name(company_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT companyName
        FROM company
        WHERE companyID = %s;
    """

    cursor.execute(query, (company_id,))
    result = cursor.fetchone()

    conn.close()
    return result


# Retrieve attendee information for a selected company
def get_attendees_by_company(company_id):
    conn = get_connection()
    cursor = conn.cursor()

    # SQL query joining multiple tables to retrieve attendee details
    query = """
        SELECT
            company.companyName,
            attendee.attendeeName,
            attendee.attendeeDOB,
            session.sessionTitle,
            session.speakerName,
            room.roomName
        FROM company
        JOIN attendee ON company.companyID = attendee.attendeeCompanyID
        JOIN registration ON attendee.attendeeID = registration.attendeeID
        JOIN session ON registration.sessionID = session.sessionID
        JOIN room ON session.roomID = room.roomID
        WHERE company.companyID = %s;
    """

    cursor.execute(query, (company_id,))
    results = cursor.fetchall()

    conn.close()
    return results


# Check if an attendee ID already exists
def attendee_exists(attendee_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT attendeeID
        FROM attendee
        WHERE attendeeID = %s;
    """

    cursor.execute(query, (attendee_id,))
    result = cursor.fetchone()

    conn.close()

    # Return True if attendee exists
    return result is not None


# Add a new attendee to the database
def add_attendee(attendee_id, name, dob, gender, company_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO attendee
        (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
        VALUES (%s, %s, %s, %s, %s);
    """

    # Execute insert query
    cursor.execute(query, (attendee_id, name, dob, gender, company_id))

    # Save changes to database
    conn.commit()

    conn.close()


# Retrieve attendee name using attendee ID
def get_attendee_name(attendee_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT attendeeName
        FROM attendee
        WHERE attendeeID = %s;
    """

    cursor.execute(query, (attendee_id,))
    result = cursor.fetchone()

    conn.close()
    return result


# Retrieve all room information from database
def get_rooms():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT roomID, roomName, capacity
        FROM room
        ORDER BY roomID;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results

# Retrieve conference summary statistics
def get_conference_summary():
    conn = get_connection()
    cursor = conn.cursor()

    summary = {}

    cursor.execute("SELECT COUNT(*) FROM attendee;")
    summary["attendees"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM company;")
    summary["companies"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM session;")
    summary["sessions"] = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM room;")
    summary["rooms"] = cursor.fetchone()[0]

    conn.close()

    return summary

# Retrieve attendees who attended the same sessions
def get_shared_session_attendees(attendee_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT DISTINCT
            attendee.attendeeID,
            attendee.attendeeName
        FROM registration r1
        JOIN registration r2
            ON r1.sessionID = r2.sessionID
        JOIN attendee
            ON r2.attendeeID = attendee.attendeeID
        WHERE r1.attendeeID = %s
        AND r2.attendeeID != %s;
    """

    cursor.execute(query, (attendee_id, attendee_id))
    results = cursor.fetchall()

    conn.close()
    return results