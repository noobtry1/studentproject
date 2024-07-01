import json 

class NoMatchingIdError(Exception):
    pass

class Teacher:

    def accept(self):
        """Accepts data from user and stores it in teacher file
        Raises:
            NoMatchingIdError: is raised when id is matched
        Returns:
            int: returns 0 if user inputs invalid data
        """
        with open('data_files/teacher.json', 'r') as file:
            data = json.load(file)
        input_dictionary = {}
        input_dictionary["name"] = input("Enter the name: ")
        input_dictionary["subject"] = input("Enter the subject: ")
        input_dictionary["id"] = int(input("Enter id: "))
        try:
            for elements in data:
                if input_dictionary['id'] == elements['id']:
                    raise NoMatchingIdError
        except NoMatchingIdError:
            print("ID already exists. Pls enter again")
            return 0 
        else:
            input_dictionary["email"] = input("Enter email id: ")
            # Checking if input email is valid
            # Valid if it contains @gmail.com or @outlook.com
            email_list = input_dictionary['email'].split('@')
            if email_list[1:] != ['gmail.com'] and email_list[1:] != ['outlook.com']:
                print("Invalid email id. Pls enter again")
                return 0
            # Input and checking if phone number is 10 digits
            input_dictionary["phone_number"] = int(input("Enter phone number: "))
            if len(str(input_dictionary['phone_number'])) != 10:
                print("Invalid phone number. Pls enter again")
                return 0
            data.append(input_dictionary) # adding user inputs stored in dictionary to the data list
            with open('data_files/teacher.json', 'w') as file:
                json.dump(data, file)
        # Checking for invalid email id

    def display_all(self) -> None:
        """Displays some records of every person
        """
        with open('data_files/teacher.json', 'r') as file:
            data = json.load(file)
            for elements in data:
                print(f"name: {elements['name']}")
                print(f"email: {elements['email']}")
                print(f"phone_number: {elements['phone_number']}")
                print(f"subject: {elements['subject']}")
                print()

    def search(self,req_name: str) -> None:
        """Displays all records of requested teacher
        Args:
            req_name (str): name of teacher
        """
        with open('data_files/teacher.json', 'r') as file:
            data = json.load(file)
        found = 0
        for elements in data:
            if elements['name'] == req_name:
                print(f"name: {elements['name']}")
                print(f"subject: {elements['subject']}")
                print(f"id: {elements['id']}")
                print(f"email: {elements['email']}")
                print(f"phone_number: {elements['phone_number']}")
                found = 1
        if found == 0:
            print(f"{req_name} not found in database")
                    
    def delete(self,req_name: str, id: int) -> None:
        with open('data_files/teacher.json', 'r') as file:
            data = json.load(file)
        found = -1   #is -1 if not found else +ve number 
        # finding the index of data to be deleted
        for index, elements in enumerate(data):
            if elements["name"] == req_name and elements['id'] == id:
                found = index
                break
        if found != -1:
            del data[found] # deletes the data of found index from the list
            with open('data_files/teacher.json', 'w') as file: # rewrites the file with deleted item from list
                json.dump(data, file)
        else:
            print(f"{req_name} not found in database")
           
