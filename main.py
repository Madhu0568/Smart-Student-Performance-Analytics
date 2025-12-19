from database import create_table, connect_db

def add_student(name, subject, marks):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)",
        (name, subject, marks)
    )
    conn.commit()
    conn.close()

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def main():
    create_table()
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            subject = input("Subject: ")
            marks = int(input("Marks: "))
            add_student(name, subject, marks)
            print("Student added successfully!")

        elif choice == "2":
            students = view_students()
            for s in students:
                print(s)

        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()