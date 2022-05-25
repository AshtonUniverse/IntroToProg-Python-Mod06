# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table".
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALarkin,5.24.2022,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoList.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def os_path_isfile(file_name):
        """ Validates if file_name exists

        :param file_name: (string) with name of file:
        :return: isfile_bln
        """
        import os.path
        isfile_bln = (os.path.isfile(file_name))
        return (isfile_bln)

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        # TODO: Add Code Here!
        priority_options = ['High', 'Medium', 'Low']  # Task priority options
        while True:
            if (task != '' and priority in priority_options):
                list_of_rows.append(row)
            elif (task == '' and priority in priority_options):
                print()  # Add an extra line for looks
                print('Empty task entered.')
            elif (task != '' and priority not in priority_options):
                print()  # Add an extra line for looks
                print('Invalid priority entered')
            elif (task == '' and priority not in priority_options):
                print()  # Add an extra line for looks
                print('Empty task and invalid priority entered.')
            else:
                break
            return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        remove_bln = False  # verify that the data was found
        for row in list_of_rows:
            if (row["Task"] == task):
                list_of_rows.remove(row)
                remove_bln = True
        # Update user on the status
        if remove_bln == True:
            print()  # Add an extra line for looks
            print(task + " removed from ToDoList. ")
        else:
            print()  # Add an extra line for looks
            print(task + " is not in ToDoList. ")
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print()  # Add an extra line for looks
        print("Data saved to file: " + "[" + file_name + "]")
        return list_of_rows

# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        ****************************
        ToDoList - Menu of Options
        ****************************
        1) Show current data
        2) Add a new Task
        3) Remove an existing Task
        4) Save Data to File        
        5) Exit Program
        ****************************
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        # TODO: Add Code Here!
        task = str(input("Enter a Task: ").strip().lower().title())
        priority = str(input("Enter a Priority: [High, Medium, Low] - ").strip().lower().title())
        return (task, priority)

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        # TODO: Add Code Here!
        task = str(input("Enter a task to remove from ToDoList: ").strip().lower().title())
        return (task)

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, load data from ToDoFile.txt if file_name exists
    isfile_bln = Processor.os_path_isfile(file_name=file_name_str)
    if (isfile_bln == True):
        Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data
    else:
        pass

while (True):
    # Step 2 - Display a menu of choices to the user
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 3 - Process user's menu choice
    if choice_str.strip() == '1':
        IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
        continue  # to show the menu

    if choice_str.strip() == '2':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue # to show the menu

    elif choice_str == '3':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '4':  # Save Data to File
        table_lst = Processor .write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '5':  # Exit Loop
        print("Goodbye!")
        break  # by exiting loop

# Exit the program
input("\nPress the enter key to exit.")
