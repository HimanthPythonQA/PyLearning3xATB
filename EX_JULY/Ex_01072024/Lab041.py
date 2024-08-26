# multiple inheritance
class father:
    def father_money(self):
        return "1lac"

    def home1(self):
        return "this is from father"


class mother:
    def mother_money(self):
        return "2lac"

    def home2(self):
        return "this is from mother"

class son(father, mother): # method resolution order(if mother is 1st then it will be mther argument 1st)
    def home3(self):
        return "this is from son"


son = son()
print(son.father_money())
print(son.mother_money())
print(son.home3())
print(son.home2())
print(son.home1())

mother = mother()
print(mother.mother_money())
print(mother.home2())

father = father()
print(father.father_money())
print(father.home1())