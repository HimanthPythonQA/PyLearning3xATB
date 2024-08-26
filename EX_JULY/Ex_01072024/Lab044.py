# POLYMORPHISM:polymorphism allows objects of different classes to be treated
# as object of a common super class
# POLYMORPHISM is utilized to create flexible and reusable code.

class shape:
    def area(self):
        print("area of shape")



class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = rectangle(3,4)
print(shape1.area())

shape2 = circle(10)
print(shape2.area())

shape3 = shape()
print(shape3.area())
