import mysql.connector

def get_mysql_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="appdbproj"
    )
    return conn


def test_connection():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendee LIMIT 5")

        results = cursor.fetchall()

        for row in results:
            print(row)

        conn.close()
        print("MySQL connection working ✅")

    except Exception as e:
        print("Error:", e)