print('Welcome to Student Management')

students = []

def menu():
    while True:
        print('\nEnter an option of your choice:')
        print('1. Add students\n2. Delete students\n3. Find student\n4. List all students\n5. Exit')
        option = input('= ')
        if option == '1':
            add()
        elif option == '2':
            delstu()
        elif option == '3':
            findstu()
        elif option == '4':
            list_students()
        elif option == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid entry, please enter a valid option.')

def add():
    try:
        num = int(input('How many students do you want to enroll? '))
        for _ in range(num):
            student = {}
            student['Name'] = input('Enter student name: ')
            student['number'] = input('Enter roll number: ')
            students.append(student)
        print('Number of students enrolled:', len(students))
    except ValueError:
        print('Please enter a valid number.')
    input('Press Enter to go back to the menu.')

def delstu():
    delnumber = input('Enter the roll number of the student whose data you want to delete: ')
    for student in students:
        if student['number'] == delnumber:
            students.remove(student)
            print(f"Student with roll number {delnumber} has been removed.")
            break
    else:
        print(f"No student found with the roll number {delnumber}.")
    input('Press Enter to go back to the menu.')

def findstu():
    findnumber = input('Enter roll number to get the student data: ')
    for student in students:
        if student['number'] == findnumber:
            print(f"Student found: Name: {student['Name']}, Roll Number: {student['number']}")
            break
    else:
        print(f"No student found with the roll number {findnumber}.")
    input('Press Enter to go back to the menu.')

def list_students():
    if not students:
        print('No students enrolled yet.')
    else:
        print('\nList of all students:')
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. Name: {student['Name']}, Roll Number: {student['number']}")
    input('Press Enter to go back to the menu.')

# Start the program by calling menu
menu()
