# hybrib inheritance:

class A:
    def methodA(self):
        return "method a"


class B(A):
    def methodB(self):
        return "method b"

class C(A):
    def methodC(self):
        return "method c"

class D(B,C):
    def methodD(self):
        return "method d"


d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())

b = B()
print(b.methodA())
print(b.methodB())

c = C()
print(c.methodA())
print(c.methodC())

a = A()
print(a.methodA())