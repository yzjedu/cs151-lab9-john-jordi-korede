# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

* Purpose: Reads the file to list
* Name: read_file_to_list
* Parameters: The file name 
* Return: The data in the file 
* Algorithm:
  * Set data into an empty list 
  * Try:
    * Open the inputted file and set it to read 
    * Have the data readlines from the inputted file
    * For i in rang of the length in the data:
      * Strip the white space for each piece of data in list "i"
    * Close the inputted file 
  * Except if File is not found:
    * Output to user: "Error: File Does Not Exist"
  * Return Data 

* Purpose:  Gets the number of tables needed 
* Name: get_num_tables
* Parameters: guest amount 
* Return: The number of tables
* Algorithm:
  * Set number of tables by doing length of guest amount and divide it by 5
  * Return num tables

* Purpose: To make tables 
* Name: make_tables
* Parameters: tables and guests 
* Return: The tables with everyone seat 
* Algorithm:
  * Set current table to 1 
  * Set current seat to 1 
  * Set index checker to 0
  * For seat in range from 0 to 5:
    * For table in range of the current table and tables + 1:
      * For i in range of the index checker and index checker + 5:
        * Output: "~~~~~~~~~~~~~~~~~~~~~~~\n" "Table "+ str(current_table) + ", Seat " + str(current_seat) + ", " + guests[i] + " \n" + "~~~~~~~~~~~~~~~~~~~~~~~"
        * Add 1 to current seat
      * Have current seat equal to 1 
      * Add 5 to the index checker
      * Add one to the current table 

* Purpose:  Gets the user input 
* Name: get_user_input
* Parameters: none
* Return: The file name 
* Algorithm:
  * Prompt the user: "Please enter the name of the file that contains the names for the party.\n"
                   "(Your options are either Nweke, Yalew, or Isaacman | Please DO NOT add '.txt' to your input) ")
  * Convert input into lowercase 
  * While the result is not "nweke" and is not "yalew" and is not "isaacman":
    * Output an empty string
    * Prompt the user: "That's not a name of a file we have\n"
                       "Please enter the name of the file that contains the names for the party.\n"
                       "(Your options are either Nweke, Yalew, or Isaacman | Please DO NOT add '.txt' to your input) ")
    * Convert input into lowercase
  * Return the input + ".txt"

* Purpose: Runs the program 
* Name: main 
* Parameters: none
* Return: none
* Algorithm:
  * Output the user: "Hello! We are organizing a party for students currently taking Computer Science 151.\n"
          "We're using this program to seat the students at their respective tables. Why not take a look?")
  * Output an empty string 
  * Have file call the read_file_to_list function with the parameter of the function get_user_input
  * Output an empty string 
  * Have tables needed call the gem_num_tables with the parameter of the file that the user inputted 
  * Output: "Number of tables:" and the tables needed
  * Output an empty string 
  * Convert input into string and prompt the user: "This may be a lot to take in so just be prepared.\n" 
              "Press enter if you're ready to see how all the tables look. "
  * Output an empty string 
  * Output to user: "Thank you for using our program, we hope to see you there!"

1. Call the main function 



