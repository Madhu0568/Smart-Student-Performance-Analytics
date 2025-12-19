import sqlite3

def connect_db():
    return sqlite3.connect("student_data.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            subject TEXT,
            marks INTEGER
        )
    """)
    conn.commit()
    conn.close()