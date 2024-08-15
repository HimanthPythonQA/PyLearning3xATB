# OS module: this module helps to interact with operating system
# OS module: helps to get working directory, we can change the directory,check the files which exists,
#  check the size and file name, check environment variablesare present or not.

import os


print(os.name)
print(os.getcwd())
print(os.listdir())
# os.mkdir("himanth")
size = os.path.getsize('Testdata.txt')
print(size)
if size != 0:
    print("file exsist")
else:
    print("file dont exist")

mtime = os.path.getmtime('Testdata.txt')
print(mtime)