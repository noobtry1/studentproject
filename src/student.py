import json

class Student():
    def find_student_index(self, data: list, student_name: str) -> int:
        """
        Finds the index of required student in the given list
        Returns:
            int: index of student
        """
        index = -1
        for idx,diction in  enumerate(data):
            if diction['name'] == student_name:
                index = idx
                break
            if index != -1:
                break
        return index
    
    def accept(self):
        """Accpets user from input and stores data in student file
        Returns:
            int: 0 if user inputs invalid data
        """
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        input_dictionary = {}
        mark_dictionary = {}
        input_dictionary["name"] = input("Enter the name: ")
        input_dictionary["phone_number"] = input("Enter phone number: ")
        # Checking if phone number is 10 digits if not making the user enter data again
        if len(str(input_dictionary['phone_number'])) != 10:
            print("Invalid phone number. Pls enter again")
            return 0
        input_dictionary["roll_number"] = int(input("Enter roll number: "))
        # Checking if the entered roll numbers is already present in the database
        for elements in data:
            if input_dictionary["roll_number"] == elements['roll_number']:
                print("Roll number already in database. Pls enter again")
                return 0
        input_dictionary["email"] = input("Enter email id: ")
        # Checking if input email is valid
        # Valid if it contains @gmail.com or @outlook.com
        email_list = input_dictionary['email'].split('@')
        if email_list[1:] != ['gmail.com'] and email_list[1:] != ['outlook.com']:
            print("Invalid email id. Pls enter again")
            return 0
        input_dictionary["address"] = input("Enter address: ")
        mark_dictionary['C'] = int(input("Enter marks in C: "))
        mark_dictionary['Maths'] = int(input("Enter marks in Maths: "))
        mark_dictionary['Physics'] = int(input("Enter marks in Physics: "))
        mark_dictionary['Biology'] = int(input("Enter marks in Biology: "))
        input_dictionary['marks'] = mark_dictionary
        data.append(input_dictionary) # adding user inputs stored in dictionary to the data list
        with open('data_files/students.json', 'w') as file:
            json.dump(data, file)
        
    def display_all(self) -> None:
        """Displays all the data
        """
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
            for diction in data:
                print(f"name: {diction['name']}")
                print(f"email: {diction['email']}")
                print(f"phone_number: {diction['phone_number']}")
                print(f"roll_number: {diction['roll_number']}")
                print(f"address: {diction['address']}")
                print(f"marks: {diction['marks']}")
                print()

    def Pass_Fail_Determination(self, student_name: str) -> int:
        """Finds whether a student has passed or failed

        Args:
            student_name (str): name of required student

        Returns:
            int: 0 if fail 1 if passed
        """
        failure = 0
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        index = self.find_student_index(data, student_name)
        for marks in data[index]['marks'].values():
            if marks < 40: # Fails if marks is less than 40
                failure = 1
                break
        return failure 

    def Highest_and_Lowest_Scores(self, student_name: str) -> None:
        """Finds the highest and lowest marks with the subject name for a certain student
        """
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        highest_subject = ""
        lowest_subject = ""
        highest = 1
        lowest = 100
        idx = self.find_student_index(data, student_name)
        # Calculating highest and lowest scores along with their respective subjects
        print(f"Marks of {student_name}: ")
        for subj, mark in data[idx]['marks'].items():
            if mark >= highest:
                highest_subject = subj
                highest = mark
            if mark <= lowest:
                lowest_subject = subj
                lowest = mark
        print(f"Highest marks in {highest_subject}: {highest}")
        print(f"Lowest marks in {lowest_subject}: {lowest}")
        
    def Percentage(self, student_name: str) ->None:
        """Finds the percentage of a student
        """
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        sum = 0
        index = self.find_student_index(data, student_name)
        for marks in data[index]['marks'].values():
            sum += marks
        print(f"Percentage of {student_name}: {sum/4}")   

    def Rank_Calculation(self, student_name: str) -> None:
        """Finds rank among peers of requested student

        Args:
            student_name (str): student name whose rank is to be determined
        """
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        index = self.find_student_index(data, student_name)
        total_marks = 0
        rank = 1
        # Calculating marks of all students and storing them in new key named "Total"
        for idx, elements in enumerate(data):
            m1, m2, m3, m4 = elements['marks'].values()   #Unzipping all the marks
            total_marks = m1 + m2 + m3 + m4
            data[idx]["Total"] = total_marks
        # Comparing total marks of required student with every other and finding rank
        for elements in data:
            if data[index]['Total'] < elements["Total"]:
                rank += 1
        print(f"Rank of {student_name}: {rank}")
    
    def student_in_database(self, student_name: str):
        """Finds if a student is in the database or not
        Returns:
            int: 0 if not in database else 1
        """
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        value = 0
        for item in data:
            if item['name'] == student_name:
                value = 1
            if value == 1:
                break
        if value == 0:
            print(f"{student_name} not found in the database")
        return value
    
    def search(self,student_name: str):
        """ Displays percentage, rank, highest and lowest scores if the student has passed
        Args:
            student_name (str): description of required student
        """
        if self.student_in_database(student_name) == 0:
            return 0
        status = self.Pass_Fail_Determination(student_name)
        self.Highest_and_Lowest_Scores(student_name)
        if(status == 1):
            print(f"{student_name} has failed")
            return 0
        else:
            print(f"{student_name} has passed")
        # Below code runs only if the student has passed
        self.Percentage(student_name)
        self.Rank_Calculation(student_name)

    def delete(self, studnet_name: str, rollno: int) -> None:
        with open('data_files/students.json', 'r') as file:
            data = json.load(file)
        found = -1
        # finding the index of data to be deleted
        for index, elements in enumerate(data):
            if elements["name"] == studnet_name and elements['roll_number'] == rollno:
                found = index
                break
        if found != -1:
            del data[found] # deletes the data of found index from the list
            with open('data_files/students.json', 'w') as file:
                json.dump(data, file)
        else:
            print(f"{studnet_name} not found in database")

