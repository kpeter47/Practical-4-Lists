
"""
CP1404/CP5632 Practical
Data file -> lists program
"""


FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)  # Append the list of parts to the data list
    input_file.close()
    return data  # Return the data list


def display_subject_details(data):
    """Display subject details."""
    for subject_info in data:
        subject_code, lecturer, student_count = subject_info
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


if __name__ == "__main__":
    main()
