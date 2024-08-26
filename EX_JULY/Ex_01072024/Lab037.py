# INHERITANCE: acquire the attributes and behaviour (data members & methods) /or
# INHERITANCE: its a concept in oops(object oriented programing) that allows a class (child class)
# to inherit attributes and methods from another class (parent class)
#
# TYPES OF INHERITANCE:
# single INHERITANCE:

# multiple INHERITANCE

# multi-level INHERITANCE

# hybrid INHERITANCE

# hierarchical INHERITANCE

class Grandparent:
    key = "abc@123"
    def grandparent_method(self):
        return "grandparents method"

class Father(Grandparent): #inheritance of Grandparent to Father)
    def parent_method(self):
        self.grandparent_method()
        return "parents method"


parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)

