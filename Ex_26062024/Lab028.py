class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# object_ref = Calc(8, 4)
# output1 = object_ref.sum()
# print(output1)
# output2 = object_ref.sub()
# print(output2)
# output3 = object_ref.mul()
# print(output3)
# output4 = object_ref.div()
# print(output4)

print(Calc(3,4).sum())
print(Calc(8,4).sub())
print(Calc(8,4).mul())
