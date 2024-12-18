# Programmers:  Jordi Korede and John
# Course:  CS151, Dr.Yalew
# Due Date: 11/14/24
# Lab Assignment: 9
# Problem Statement: Organizing a dinner party with assigned seats.
# Data In: The filename that the user inputs
# Data Out: The names of everyone on the inputted file with their seat number and table number
# Credits: Class
# Input Files: We need either yalew,nweke, or isaacman in order for this code to work


# Purpose:  Reads the file to list
# Parameters: The file name
# Return: The data in the file
def read_file_to_list(filename):
    data = []
    try:
        input_file = open(filename, "r")
        data = input_file.readlines()
        for i in range(len(data)):
            data[i] = data[i].strip()
        input_file.close()
    except FileNotFoundError:
        print("Error: File Does Not Exist")
    return data

# Purpose: Gets the number of tables needed
# Parameters: The guest amount
# Return: The number of tables
def get_num_tables(guest_amount):
    num_tables = int(len(guest_amount) / 5)
    return num_tables

# Purpose: Makes the tables
# Parameters: Tables and guests
# Return: The table with everyone's seat
def make_tables(tables, guests):
    current_table = 1
    current_seat = 1
    index_checker = 0
    for seat in range(0, 5):
        for table in range(current_table, tables + 1):
            for i in range(index_checker, index_checker + 5):
                print("~~~~~~~~~~~~~~~~~~~~~~~\n"
                      "Table " + str(current_table) + ", Seat " + str(current_seat) + ", " + guests[i] + " \n"
                      "~~~~~~~~~~~~~~~~~~~~~~~")
                current_seat += 1
            current_seat = 1
            index_checker += 5
            current_table += 1

# Purpose: Gets the user input
# Parameters: None
# Return: The file name
def get_user_input():
    result = input("Please enter the name of the file that contains the names for the party.\n"
                   "(Your options are either Nweke, Yalew, or Isaacman | Please DO NOT add '.txt' to your input) ")
    result = result.lower()
    while result != "nweke" and result != "yalew" and result != "isaacman":
        print("")
        result = input("That's not a name of a file we have\n"
                       "Please enter the name of the file that contains the names for the party.\n"
                       "(Your options are either Nweke, Yalew, or Isaacman | Please DO NOT add '.txt' to your input) ")
        result = result.lower()
    return result + ".txt"

# Purpose: Runs the program
# Parameters: None
# Return: None
def main():
    print("Hello! We are organizing a party for students currently taking Computer Science 151.\n"
          "We're using this program to seat the students at their respective tables. Why not take a look?")
    print("")
    file = read_file_to_list(get_user_input())
    print("")
    tables_needed = get_num_tables(file)
    print("Number of tables: ", tables_needed)
    print("")
    str(input("This may be a lot to take in so just be prepared.\n" 
              "Press enter if you're ready to see how all the tables look. "))
    make_tables(tables_needed, file)
    print("")
    print("Thank you for using our program, we hope to see you there!")

main()

