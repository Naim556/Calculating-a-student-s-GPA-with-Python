def calculate_gpa():
    scores = []

    while True:
        try:
            grade = input("Enter a grade (or type -1 to finish): ")
            if grade == "-1":
                break
            grade = float(grade)
            if grade < 0:
                print("Grade cannot be negative. Please enter a valid score.")
                continue

            scores.append(grade)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if scores:
        average = sum(scores) / len(scores)
        return average
    else:
        print("No valid grades entered.")
        return None

def main():
    students_gpa = []
    print("Hello, welcome! This tool calculates a student's GPA.")

    while True:

        student_name_get = input("Please enter the student's name: ").strip()
        if not student_name_get:
            print("Student name cannot be empty.")
            continue

        while True:
            gpa = calculate_gpa()
            if gpa is not None:
                print(f"{student_name_get}'s GPA: {gpa:.2f}")
                students_gpa.append({"name": student_name_get, "gpa": gpa})
                break

        continue_or_end = input("Do you want to continue[Y|N]? ")

        if continue_or_end.capitalize() == "N":
            print("end :)")
            break
        elif continue_or_end.capitalize() != "Y":
            print("Invalid choice. Ending the process.")
            break


    print("\nSummary of Students' GPAs:")
    sorted_students = sorted(students_gpa, key=lambda x: x['gpa'], reverse=True)
    for student in sorted_students:
        print(f"- {student['name']}: {student['gpa']:.2f}")

if __name__ == "__main__":
    main()