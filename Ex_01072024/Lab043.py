def multiple_return_one():
    return 99,"himanth",False

print(multiple_return_one())





class grandfather:
    key_gold = "1kg"
    def house(self):
        return "grandfather method"


class father(grandfather):
    car_world = "bmw"
    # def house(self):
    #     return "father method"

class son(father):
    gun_gallery = "M4 pistol"
    # def house(self):
    #     return "son method"


son = son()
print(son.house())