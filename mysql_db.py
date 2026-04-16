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