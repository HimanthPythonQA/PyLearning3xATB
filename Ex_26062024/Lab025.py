# CLASS is a group of objects which have some properties & functions(called methods). when a class is created no memory is allocated
# CLASS is a blue print to create an object

# OBJECT is an instance of class. all data members & member functions of the class can be accessed with the help of objects
# OBJECT are allocated memory space whenever they are created.

class person:
    name = None
    id = None
    age = None
    Phone_num = None

    def walk(self):
        print("I am walking")

    def talk(self):
        print("I am talking")

    def another(self):
        print("I am method")

    def sleep(self, name):
        print("I am a method")
        print("sleep", name)

    def sleep1(self, name):
        print("I am a method")
        return None


himanth = person()
himanth.name = "Dasari himanth"
himanth.talk()
himanth.walk()


hemanth = person()
hemanth.name = "Dasari hemanth"
hemanth.another()
hemanth.talk()


# create object of the person class
# objectref = object  ----> class name()
