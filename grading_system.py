GRADE_SCALE = ["D1", "D2", "C3", "C4", "C5", "C6", "P7", "P8", "F9"]
GRADE_VALUES = {grade: index + 1 for index, grade in enumerate(GRADE_SCALE)}
GRADE_THRESHOLDS = [80, 75, 70, 65, 60, 50, 45, 40]
SUBJECT_NAMES = ["Math", "Science", "SST", "English"]
FILE_PATH = "grades.txt"


def get_grade(mark):
    for threshold, grade in zip(GRADE_THRESHOLDS, GRADE_SCALE):
        if mark >= threshold:
            return grade
    return GRADE_SCALE[-1]


def print_and_save_grades(name, subjects, file_path=FILE_PATH):
    total_aggregate = 0

    print(f"\n{name.upper()} HAS GOT THE FOLLOWING MARKS AND GRADES\n")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"Name: {name}\n")

        for subject, mark in subjects.items():
            grade = get_grade(mark)
            total_aggregate += GRADE_VALUES[grade]
            file.write(f"{subject}: {grade}\n")
            print(f"{subject} ==> {grade}")

        file.write(f"Total Aggregate: {total_aggregate}\n\n")

    print(f"\nTotal Aggregate: {total_aggregate}")


def collect_subject_marks():
    subjects = {}
    for subject in SUBJECT_NAMES:
        subjects[subject] = int(input(f"Enter marks for {subject}: "))
    return subjects


def main():
    while True:
        name = input("Enter the student's name: ")
        subjects = collect_subject_marks()
        print_and_save_grades(name, subjects)

        if input("Do you wish to continue (yes/no): ").strip().lower() != "yes":
            print("GOODBYE")
            break


if __name__ == "__main__":
    main()
