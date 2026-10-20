"""Student Grade Analyzer

Completed version of the starter code. 
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if grade >= 90:
        return ("Excellent", "Passed")
    elif grade >= 85:
        return ("Very Good", "Passed")
    elif grade >= 80:
        return ("Good", "Passed")
    elif grade >= 75:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                # Skip blank lines
                if line == "":
                    continue

                # Skip comment lines (used in grades.txt for notes)
                if line.startswith("#"):
                    continue

                fields = line.split(",")

                # Must have exactly 3 fields: student_id, name, grade
                if len(fields) != 3:
                    continue

                student_id = fields[0].strip()
                name = fields[1].strip()
                grade_text = fields[2].strip()

                # Skip records with a missing id or name
                if student_id == "" or name == "":
                    continue

                # Convert and validate the grade
                try:
                    grade = float(grade_text)
                except ValueError:
                    continue

                if grade < 0 or grade > 100:
                    continue

                students.append({
                    "student_id": student_id,
                    "name": name,
                    "grade": grade
                })

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        total_grade += student["grade"]

        _, status = classify_grade(student["grade"])
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if student["grade"] > highest_student["grade"]:
            highest_student = student

        if student["grade"] < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    return {
        "total_students": len(students),
        "average": average,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No student records to display.")
        return

    print()
    print(f"{'Student No.':<12} {'Name':<20} {'Grade':<8} {'Classification':<20} {'Status'}")
    print("-" * 75)

    for student in students:
        classification, status = classify_grade(student["grade"])
        name_display = student["name"][:18]  # slice for fixed-width display

        print(f"{student['student_id']:<12} {name_display:<20} "
              f"{student['grade']:<8.2f} {classification:<20} {status}")

    print()


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if statistics is None:
        print("No statistics available.")
        return

    print()
    print("CLASS STATISTICS")
    print(f"Number of students: {statistics['total_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed_count']}")
    print(f"Failed: {statistics['failed_count']}")
    print(f"Highest: {statistics['highest_student']['name']} - "
          f"{statistics['highest_student']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest_student']['name']} - "
          f"{statistics['lowest_student']['grade']:.2f}")
    print()


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []
    keyword = keyword.strip().lower()

    for student in students:
        id_lower = student["student_id"].lower()
        name_lower = student["name"].lower()

        if keyword in id_lower or keyword in name_lower:
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
        with open(filename, "w") as file:
            file.write("STUDENT GRADE ANALYZER - REPORT\n")
            file.write("=" * 40 + "\n\n")

            file.write("ALL STUDENT RECORDS\n")
            file.write("-" * 40 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(
                    f"{student['student_id']} - {student['name']} - "
                    f"{student['grade']:.2f} - {classification} - {status}\n"
                )

            file.write("\nCLASS STATISTICS\n")
            file.write("-" * 40 + "\n")
            file.write(f"Number of students: {statistics['total_students']}\n")
            file.write(f"Class average: {statistics['average']:.2f}\n")
            file.write(f"Passed: {statistics['passed_count']}\n")
            file.write(f"Failed: {statistics['failed_count']}\n")
            file.write(f"Highest: {statistics['highest_student']['name']} - "
                       f"{statistics['highest_student']['grade']:.2f}\n")
            file.write(f"Lowest: {statistics['lowest_student']['name']} - "
                       f"{statistics['lowest_student']['grade']:.2f}\n")

        print(f"Report successfully saved to '{filename}'.")

    except OSError:
        print(f"Error: Could not write to file '{filename}'.")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            statistics = calculate_statistics(students)
            display_statistics(statistics)

        elif choice == "3":
            keyword = input("Enter student number or name to search: ").strip()
            results = search_student(students, keyword)
            if not results:
                print(f"\nNo matching student found for '{keyword}'.")
            else:
                display_students(results)

        elif choice == "4":
            statistics = calculate_statistics(students)
            save_report(students, statistics, "grade_report.txt")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
