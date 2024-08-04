# how to open a file in python
try:
    file = open('himanth.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("file not found, please check path")
finally:
    file.close()
