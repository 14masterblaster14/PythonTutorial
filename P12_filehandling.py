#############################
#
#   # File Handling :   Operations
#                       -   Create
#                       -   Write
#                       -   Read
#                       -   Update (append / overwrite)
#                       -   Delete
#############################


#####
# open() : File Opening
#
#          Modes :
#                   "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#                   "a" - Append - Opens a file for appending, creates the file if it does not exist
#                   "w" - Write - Opens a file for writing, creates the file if it does not exist
#                   "x" - Create - Creates the specified file, returns an error if the file exists
#
#                   "t" - Text - Default value. Text mode
#                   "b" - Binary - Binary mode (e.g. images)
#
#####


fi = open("demofile.txt")  # Equal to      fi = open("demofile.txt","rt")

# O/P : If File not present
# FileNotFoundError: [Errno 2] No such file or directory: 'demofile.txt'


#####
# create() :
#           To create a new file in Python, use the open() method, with one of the following parameters:
#                   "x" - Create - will create a file, returns an error if the file exist
#                   "a" - Append - will create a file if the specified file does not exist
#                   "w" - Write - will create a file if the specified file does not exist
#####

# f9 = open("myfile_create.txt","x")
# f9.close()
f8 = open("myfile_append.txt", "a")
f7 = open("myfile_write.txt", "w")

#####
# write() :
#           To write to an existing file, you must add a parameter to the open() function:
#                   "a" - Append - will append to the end of the file
#                   "w" - Write - will overwrite any existing content
#####

f8.write("We have added one line through Append operation")
f8.close()

f7.write("We have added one line through overwrite operation")
f7.close()

"""
### demofile.txt ###
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

#####
# read() : By default the read() method returns the whole text, but you can also specify how many characters you want to return:
#####

## Read block
fileName = "demofile.txt"
f1 = open(fileName, "r")
data = f1.read()
f1.close()
print(data)

""" 
O/P : 
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

print(f1.read(5))  # Return the 5 first characters of the file. O/P : Hello

## Read Line by line

print(f1.readline())  # O/P : Hello! Welcome to demofile.txt
print(f1.readline())
print(f1.readline())

"""
O/P : 
Hello! Welcome to demofile.txt
This file is for testing purposes.
"""

for x in f1:
    print(x)

""" 
O/P : 
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

#####
# delete () : To delete a file, you must import the OS module, and run its os.remove() function
#####

import os

# os.remove("myfile_create.txt")

## Check if File exist:

if os.path.exists("myfile_create.txt"):
    print("The file exist in the system")
#  os.remove("myfile_create.txt")
else:
    print("The file does not exist")

## Delete folder  :

# os.mkdir("myfolder")
# os.rmdir("myfolder")

# os.mkdir("D:\DESKTOP\python\myfolder\myfolder",000000)
os.rmdir("D:\DESKTOP\python\myfolder\myfolder")
