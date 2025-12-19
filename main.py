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

def calculate_average():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(marks) FROM students")
    avg = cursor.fetchone()[0]
    conn.close()
    return avg

def top_performer():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name, subject, marks FROM students ORDER BY marks DESC LIMIT 1"
    )
    top = cursor.fetchone()
    conn.close()
    return top

def grade_student(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

def main():
    create_table()

    while True:
        print("\n===== Student Performance Analytics =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Average Marks")
        print("4. Top Performer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            subject = input("Subject: ")
            marks = int(input("Marks: "))
            add_student(name, subject, marks)
            print("Student added successfully!")

        elif choice == "2":
            students = view_students()
            for s in students:
                grade = grade_student(s[3])
                print(f"Name: {s[1]}, Subject: {s[2]}, Marks: {s[3]}, Grade: {grade}")

        elif choice == "3":
            avg = calculate_average()
            if avg:
                print(f"Average Marks: {round(avg, 2)}")
            else:
                print("No records found.")

        elif choice == "4":
            top = top_performer()
            if top:
                print(
                    f"Top Performer → Name: {top[0]}, Subject: {top[1]}, Marks: {top[2]}"
                )
            else:
                print("No records found.")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
