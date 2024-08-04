# file handling
# how to read a text, and write into it using python code

# Mode:-
# r for reading (default)
# w for writing (create a new file or turncates an existing one)
# a for appending
# b for binary mode zoom.exe
# + for updating (reading,writing)


# read and write content
# read a file
# read entire content: content = file_object.read()
# line = file_object.readline() for single line
# line = file_object.readline() for all lines in a list
# close the file.
import os
print(os.getcwd())
cwd = os.getcwd()
file = open("TestData.txt",'r')
content = file.read()
print(content)
file.close()
