# method overriding: same name in the parent and child class, child will always over ride the parent function
# some times we use key word call super ( super means call my parent function)

class father:
    def home(self):
        print("1bhk")

class son(father):
   #pass
    def home(self):
        super().home()
        print("3bhk")

himanth = son()
print(himanth.home())


# method overloading: same name but different arguments

class math_util:
    def add(self,a, b=0, c=0):
        return a + b + c


M = math_util()
op1 = M.add(1)
op2 = M.add(1,2)
op3 = M.add(1,2,3)

print(op1)
print(op2)
print(op3)