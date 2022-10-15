# write a program that will save the names of students in a text file. 
# option one should be to add students and option two will be to disply all students. 

file = open('student_name.txt', 'a')

while True: 
    print("Enter 1 to add students")
    print("Enter 2 to display all students")
    print("Enter 3 to empty the text file")
    print("Enter anything else to break")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        file = open("student_name.txt", 'a')
        student_name = input("Enter the student name: ")
        student_name += '\n'
        file.write(student_name)
        file.close()
    elif choice == 2: 
        file = open('student_name.txt', 'r')
        lines = file.readlines()
        student_name = []
        for students in lines:
            students = students.rstrip()
            student_name.append(students)
        print(student_name)
        file.close()
    elif choice == 3:
        file = open('student_name.txt', 'w')
        file.write(' ')
        file.close()
        


    else:
        break
