# # Match
numbers = int(input("enter the numbers\n"))
match numbers:
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered 2")

    case 3:
        print("you have entered 3")

    case 4:
        print("you have entered 4")

    case _:
        print("no idea")



def greet():
    print("hello world")

greet()

def greet(name):
    print("your name is",name)

greet("yeddava")


def allowed_to_attend_python_classes(name, password):
    if name == "himanth":
        if password == "yes":
            print("you are allowed to enter")
        else:
            print("you are not allowed to enter")


allowed_to_attend_python_classes("himanth", "yes")
