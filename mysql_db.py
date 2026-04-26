import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="appdbproj"
    )

def test_mysql_connection():
    try:
        conn = get_connection()
        conn.close()
        return True
    except Exception as e:
        print("MySQL connection error:", e)
        return False
        
def search_speakers_sessions(search_text):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT 
            session.speakerName,
            session.sessionTitle,
            room.roomName
        FROM session
        JOIN room ON session.roomID = room.roomID
        WHERE session.speakerName LIKE %s;
    """

    cursor.execute(query, (f"%{search_text}%",))
    results = cursor.fetchall()

    conn.close()
    return results