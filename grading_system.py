def get_grade(value, grade_scale):
    if value >= 80:
        return grade_scale[0]  # D1
    elif value >= 75:
        return grade_scale[1]  # D2
    elif value >= 70:
        return grade_scale[2]  # C3
    elif value >= 65:
        return grade_scale[3]  # C4
    elif value >= 60:
        return grade_scale[4]  # C5
    elif value >= 50:
        return grade_scale[5]  # C6
    elif value >= 45:
        return grade_scale[6]  # P7
    elif value >= 40:
        return grade_scale[7]  # P8
    else:
        return grade_scale[8]  # F9

def get_grade_value(grade, grade_values):
    return grade_values[grade]

def print_and_save_grades(name, subjects, grade_scale, grade_values, file_path):
    result_list = []
    total_aggregate = 0

    print(f"\n{name.upper()} HAS GOT THE FOLLOWING MARKS AND GRADES\n")

    with open(file_path, 'a') as file:  # Open file in append mode
        file.write(f"Name: {name}\n")
        for key, value in subjects.items():
            grade = get_grade(value, grade_scale)
            grade_value = get_grade_value(grade, grade_values)
            total_aggregate += grade_value
            file.write(f"{key}: {grade}\n")
            result_list.append(grade)
            print(f"{key} ==> {grade}")

        file.write(f"Total Aggregate: {total_aggregate}\n")
        file.write("\n")  # Add a newline for separation between entries
        print(f"\nTotal Aggregate: {total_aggregate}")

    return result_list

def main():
    while True:
        name = input("Enter the student's name: ")
        subjects = {}
        subject_names = ["Math", "Science", "SST", "English"]

        for subject in subject_names:
            mark = int(input(f"Enter marks for {subject}: "))
            subjects[subject] = mark

        grade_scale = ["D1", "D2", "C3", "C4", "C5", "C6", "P7", "P8", "F9"]
        grade_values = {"D1": 1, "D2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "P7": 7, "P8": 8, "F9": 9}
        file_path = "grades.txt"

        result_list = print_and_save_grades(name, subjects, grade_scale, grade_values, file_path)

        continue_input = input("Do you wish to continue (yes/no): ").lower()
        if continue_input != "yes":
            print("GOODBYE")
            break

if __name__ == "__main__":
    main()