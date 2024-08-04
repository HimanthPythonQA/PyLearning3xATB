class XYZ:


    def f1(self):
        try:
            a = int(input("enter the number"))
        except Exception as e:
            print("Enter only int value of a")
        else:
            print(a)
        finally:
            print("any how i will be executed")



x = XYZ()
x.f1()
