# hierarchical INHERITANCE: 1 father, multiple children
class father:

    def BHK1(self):
        print("1BHK")


class himanth(father):
    def BHK2(self):
        print("2BHK")


class hemanth(father):

    def BHK3(self):
        print("3BHK")


class tagore(father):
    def BHK4(self):
        print("BHK4")


himanth = himanth()
himanth.BHK2()
himanth.BHK1()

hemanth = hemanth()
hemanth.BHK3()
hemanth.BHK1()

tagore = tagore()
tagore.BHK4()
tagore.BHK1()