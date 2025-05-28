# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   S. Taushanoff 5/27/25 Complete Assignment
# ------------------------------------------------------------------------------------------ #
import json

# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"
# Define the Data Variables and constants
student_data: list = []  # a table of student data
MENU: str = '''


---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
#Classes

#File Processor has the functions for screen input, output & file reading & writing
class FileProcessor:

    # Output the student course/data list
    @staticmethod
    def out_stucourses(student_data: list):
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

        IO.in_menu_choice()


    # User inputs information about student
    @staticmethod
    def in_studata(student_data: list):
        print(student_data)
        print("Iput student data:")
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_dict = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student_dict)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            IO.in_menu_choice()

        except ValueError as e:
            IO.out_err_mess("Technical Error Message:", e)

        except Exception as e:
            IO.out_err_mess("Problem with data input", e)
            print("Error: There was a problem with your entered data.")

    # read the JSON file
    @staticmethod
    def read_data_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")

            temp = json.loads(file.read())
            for item in temp:

                student_data.append(item)

            file.close()
            return student_data

        except Exception as e:
            IO.out_err_mess("File does not exist.", e)
            file = open(file_name, "w")
            print("Empty file created.")

        finally:

            if file.closed == False:
                file.close()

    # Update the JSON file with user input
    @staticmethod
    def write_data_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.out_err_mess("Problem writing to file", e)
            IO.out_err_mess("Check file not in use by another program.")
        IO.in_menu_choice()

    pass

#Class IO handles interaction with the user, including prompts & exceptions
class IO:

    # Establish some output error messages
    @staticmethod
    def out_err_mess(message: str, error: Exception = None):
        print(message + "\n")

        if error != None:
            print("Technical Message\n")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def out_menu(menu: str):

        if menu == "1":
            print("Selection was " + menu)
            FileProcessor.in_studata(student_data)

        elif menu == "2":
            print("Selection was " + menu)
            FileProcessor.out_stucourses(student_data)
        elif menu == "3":
            print("Selection was " + menu)
            FileProcessor.write_data_file(FILE_NAME, student_data)
        else:
            print("Exiting Program")
            #if file.closed == False:
               # file.close()

            exit()


    @staticmethod
    def in_menu_choice():
        print(MENU)
        menu_choice: str = input("What would you like to do: ")

        if menu_choice in ['1', '2', '3', '4']:
            IO.out_menu(menu_choice)
            pass
        else:
            IO.out_err_mess("Invalid choice. Please choose from the menu.")
            IO.in_menu_choice()

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# Ask for first input
print("Program Starting...")
student_data = FileProcessor.read_data_file(FILE_NAME, student_data)
IO.in_menu_choice()
