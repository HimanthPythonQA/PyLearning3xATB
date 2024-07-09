class vwo_login:
    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name


    def login_conf(self):
        if self.__email == "himanth@gmail.com" and self.__password == "123":
            print("allowed")
        else:
            print("not allowed")


page = vwo_login("himanth@gmail.com","123", "himanth")
page.login_conf()
print(page.name)
