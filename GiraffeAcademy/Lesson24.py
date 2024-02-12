# "r" --> stands for read
# "w" --> stands for write
# "a" --> stands for append - you can add new information
# "r+" --> read and write in one

employee_file = open("The Office.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()  # --> always close a file when you open it !!!

#print(employee_file.readlines()[1])  # --> prints a specific line from the array with index "1"

# print(employee_file.readable())  # --> "readable" gets back a boolean value

# print(employee_file.readline())  # --> "readline" reads the first line and moves a little cursor onto the next line

# print(employee_file.readline())  # --> prints out the second line of the file

# print(employee_file.readlines())  # --> prints out all lines in an array

# print(employee_file.read())  # --> "read" spits out the entire file
