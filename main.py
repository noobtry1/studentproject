import src

print("----------Welcome To The Student Data Management Program---------")
resume = 'y'
while resume == 'y':
    choice = int(input("1.View Teacher Records \n2.View Student Records\n3.Edit Data\n"))
    if choice == 1:
        teacher_obj = src.Teacher()
        option = input("a.Search \nb.See all records\n")
        if option == 'a':
            input_name = input("Enter the name: ")
            teacher_obj.search(input_name)
        elif option == 'b':
            teacher_obj.display_all()
            pass
        else:
            print("Invalid choice")
    elif choice == 2:
        student_obj = src.Student()
        option = input("a.See all records \nb.Search a students record \n")
        if option == 'a':
            student_obj.display_all()
        elif option == 'b':
            name = input("Enter name: ")
            student_obj.search(name)
        else:
            print("Invalid choice")
    elif choice == 3:
       src.Authenticate()
    else:
        print("Invalid choice")
    resume = input("Continue y/n?: ")
    print("----------------------------")
              



