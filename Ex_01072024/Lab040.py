# multi level heritance e.g grand father gives to father, father gives to child
class grandfather:
    key_gold = "1kg"
    def house(self):
        return "grandfather method"


class father(grandfather):
    car_world = "bmw"
    def room(self):
        return "father method"

class son(father):
    gun_gallery = "M4 pistol"
    def hall(self):
        return "son method"



son = son()
print(son.hall())
print(son.room())
print(son.house())
print(son.key_gold)
print(son.car_world)
print(son.gun_gallery)


father = father()
print(father.room())
print(father.house())
print(father.key_gold)
print(father.car_world)


grandfather = grandfather()
print(grandfather.house())
print(grandfather.key_gold)
