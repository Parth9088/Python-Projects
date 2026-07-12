# ==========================================
# STUDENT MANAGEMENT SYSTEM (Python Only)
# ==========================================

students = []


# -------------------------------
# Add Student
# -------------------------------
def add_student():
    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students.append(student)

    print("\n✅ Student Added Successfully!\n")


# -------------------------------
# View Students
# -------------------------------
def view_students():

    if len(students) == 0:
        print("\nNo Student Records Found.\n")
        return

    print("\n------ Student Records ------")

    for student in students:
        print(f"""
Roll No : {student['Roll']}
Name    : {student['Name']}
Age     : {student['Age']}
Course  : {student['Course']}
Marks   : {student['Marks']}
Grade   : {calculate_grade(student['Marks'])}
-------------------------------
""")


# -------------------------------
# Search Student
# -------------------------------
def search_student():

    roll = input("Enter Roll Number: ")

    for student in students:

        if student["Roll"] == roll:
            print("\nStudent Found\n")
            print(student)
            return

    print("Student Not Found.")


# -------------------------------
# Update Student
# -------------------------------
def update_student():

    roll = input("Enter Roll Number: ")

    for student in students:

        if student["Roll"] == roll:

            print("\nEnter New Details")

            student["Name"] = input("Name: ")
            student["Age"] = input("Age: ")
            student["Course"] = input("Course: ")
            student["Marks"] = float(input("Marks: "))

            print("\nStudent Updated Successfully!")
            return

    print("Student Not Found.")


# -------------------------------
# Delete Student
# -------------------------------
def delete_student():

    roll = input("Enter Roll Number: ")

    for student in students:

        if student["Roll"] == roll:
            students.remove(student)
            print("\nStudent Deleted Successfully!")
            return

    print("Student Not Found.")


# -------------------------------
# Grade Calculator
# -------------------------------
def calculate_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# -------------------------------
# Show Topper
# -------------------------------
def topper():

    if len(students) == 0:
        print("No Student Records.")
        return

    top = max(students, key=lambda x: x["Marks"])

    print("\n🏆 Topper")
    print("--------------------")
    print("Name :", top["Name"])
    print("Marks:", top["Marks"])
    print("Grade:", calculate_grade(top["Marks"]))


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("""
====================================
    STUDENT MANAGEMENT SYSTEM
====================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Topper
7. Exit
====================================
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        topper()

    elif choice == "7":
        print("\nThank You!\n")
        break

    else:
        print("Invalid Choice.")