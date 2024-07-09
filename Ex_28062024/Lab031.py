# ENCAPSULATION:- binding the data variables with the methods.  /or
# hiding the data members(class variables,instance variables) by using only the methods
# in ENCAPSULATION we can mark class,variables,methods as PUBLIC,PROTECTED,PRIVATE

class car:
    name = None


    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass@123"


    def __private_method(self):
        print("protected")


    def print_name(self):
        self.__private_method()
        print("iam allowed")
        if self.__private_var == "123":
            print("123")


alto = car()
alto.print_name()
