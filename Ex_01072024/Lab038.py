class parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")


class child(parent):

    def BHK3(self):
        print("3BHK")


child_object = child()
child_object.BHK3()
child_object.BHK2()
print(child_object.gold)