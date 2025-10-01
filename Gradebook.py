# -----------------------------
# Student Gradebook System
# -----------------------------

# Store students and their subjects/grades
students = {}

# Menu options
menu = {
    1: "Add Student",
    2: "View Students",
    3: "Calculate Average",
    4: "Find Top Student",
    5: "Quit"
}

while True:
    print("\n--- Student Gradebook ---")
    for number, action in menu.items():
        print(f"{number}. {action}")

    # Get user choice
    choice = int(input("Choose an option: "))

    # Option 1: Add Student
    if choice == 1:
        name = input("Enter student name: ")
        subject = input("Enter subject: ")
        grade =input("Enter grade: ")


        # Add student and grade
        if name not in students:
            students[name] = {}
        students[name][subject] = grade

        print(f"Added {subject} grade {grade} for {name}.")

    # Option 2: View Students
    elif choice == 2:
        if not students:
            print("No students added yet.")
        else:
            for name, subjects in students.items():
                print(f"\n{name}:")
                for sub, grade in subjects.items():
                    print(f"   {sub} - {grade}")

    # Option 3: Calculate Average
    elif choice == 3:
        name = input("Enter student name: ")
        if name in students:
            grades = list(students[name].values())
            average = sum(grades) / len(grades)
            print(f"{name}'s average grade = {average:.2f}")
        else:
            print("Student not found.")

    # Option 4: Find Top Student
    elif choice == 4:
        if not students:
            print("No students available.")
        else:
            top_student = None
            top_average = 0
            for name, subjects in students.items():
                grades = list(subjects.values())
                avg = sum(grades) / len(grades)
                if avg > top_average:
                    top_average = avg
                    top_student = name
            print(f"Top student is {top_student} with an average of {top_average:.2f}")

    # Option 5: Quit
    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again!")
