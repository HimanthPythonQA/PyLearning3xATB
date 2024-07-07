# CONSTRUCTOR is a special method that is automatically called when an object is created from a class.
# CONSTRUCTOR can initialize the values and can initialize the instance variables(attributes)
class Dog:
    name = None
    id = None

    def sleep(self):
        print("sleeping")

    def _init_(self,name,id):
        self.name = name
        self.id = id

dog1 = Dog()
print(dog1.name)
print(dog1.id)

dog1.name = "chow chow"
dog1.id = 222
dog1.sleep()
print(dog1.name)
print(dog1.id)


dog2 = Dog()
print(dog2.name)
print(dog2.id)

dog2.name = "retriver"
dog2.id = 777
dog2.sleep()
print(dog2.name)
print(dog2.id)