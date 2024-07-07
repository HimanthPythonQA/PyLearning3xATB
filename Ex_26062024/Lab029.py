class Student:

    def __init__(self):
        self.name = input("enter the name")
        self.age = input("enter the age")

    def display(self):
        print(f"name is {self.name}, age is {self.age}")


student = Student()
student.display()