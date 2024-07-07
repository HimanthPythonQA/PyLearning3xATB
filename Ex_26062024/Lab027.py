class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id
    def sleep(self):
        print("sleeping  " + self.name)


dog1 = Dog("american","11")
dog2 = Dog("pitbull","13")

print(f'{dog1.name} has id {dog1.id}')
print(f'{dog2.name} has id {dog2.id}')

dog1.sleep()
dog2.sleep()




class Calc:
    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

object_ref = Calc()
output1 = object_ref.sum(8,4)
output2 = object_ref.sub(8,4)
output3 = object_ref.mul(8,4)
output4 = object_ref.div(8,4)
print(output1)
print(output2)
print(output3)
print(output4)
output1 = object_ref.sum(8,4)
