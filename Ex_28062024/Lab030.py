class Car:
    name = None
    model = None
    make = None

    def __init__(self, o_name, o_model, o_make):
        self.name = o_name
        self.model = o_model
        self.make = o_make

    def start_engine(self):
        print("starting a car with name " + self.name)
        print("starting a car with model " + self.model)
        print("starting a car with make " + self.make)


lambo = Car(o_name="lambo", o_model="2024", o_make="v12")
lambo.start_engine()

XUV_700 = Car(o_name="XUV_700", o_model="2023", o_make="v6")
XUV_700.start_engine()


class criologin:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password


    def login(self):
        if self.password == "pass123":
            print("allowed to login")

        else:
            print("not allowed")



hemanth = criologin(email="hemanth@gmail.com", password="123")
hemanth.login()

himanth = criologin(email="himanth@gmail.com", password="pass123")
himanth.login()






himanth = criologin(email="himanth@gmail.com", password="pass123")
himanth.login
