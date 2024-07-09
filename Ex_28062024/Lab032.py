class Myclass:


    def public_func(self):
        print("public function")


    def __private_func(self):
        print("this is private mrthod")


    def public_fn_private(self):
        self.__private_func()


web = Myclass()
web.public_func()
web.public_fn_private()
