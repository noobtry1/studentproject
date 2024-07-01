import json
from src.teacher import Teacher
from src.student import Student

class AuthenticationError(Exception):
    pass

def Authenticate():
    print("Verify yourself as a teacher")
    name = input("Enter your name: ")
    id = int(input("Enter your id: "))
    with open('data_files/teacher.json', 'r') as file:
        data = json.load(file)
    failure = 1
    try:
        for elements in data:
            if name == elements['name'] and id == elements['id']:
                failure = 0
                break
        if failure == 1:
            raise AuthenticationError
    except AuthenticationError:
        print("Error finding you in database. You are not eligible to cause changes.")
    else:
        print(f"\nWelcome {name}!")
        option = int(input("1.Enter Teacher Data \n2.Enter Student Data: \n3.Delete Teacher Data \n4.Delete Student Data\n"))
        teacher_obj = Teacher()
        student_obj = Student()
        if option == 1:
            while teacher_obj.accept() == 0: #Just calling the function again if it returns 0 which is an error
                pass
        elif option == 2:
            while student_obj.accept() == 0: #Just calling the function again if it returns 0 which is an error
                pass
        elif option == 3:
            del_name = input("Enter teacher name: ")
            del_id = int(input("Enter teacher id: "))
            teacher_obj.delete(del_name, del_id)
        elif option == 4:
            del_name = input("Enter student name: ")
            del_id = int(input("Enter roll number: "))
            student_obj.delete(del_name, del_id)
        else:
            print("Invalid option")

