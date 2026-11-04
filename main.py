# Student Grade Calculator
# Python Debugging and Troubleshooting Project

def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


def calculate_grade(average):

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def main():

    print("===== Student Grade Calculator =====")

    name = input("Enter student name: ")

    try:
        marks_input = input("Enter marks separated by commas: ")
        marks = [float(mark.strip()) for mark in marks_input.split(",")]

    except ValueError:
        print("Error: Please enter numeric marks only.")
        return

    if not marks:
        print("Error: Please enter at least one mark.")
        return

    if not all(0 <= mark <= 100 for mark in marks):
        print("Error: Marks must be between 0 and 100.")
        return

    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n===== Student Result =====")
    print("Student Name:", name)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    main()