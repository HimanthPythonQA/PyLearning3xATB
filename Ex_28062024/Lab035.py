class Bank_account:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdrawl(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("your balance is", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("not allowed")

    def if_you_are_auth_user(self,auth,amount):
        if auth:
            self.__withdrawl(amount)
        else:
            print("not allowed")


icic_bank = Bank_account()
icic_bank.deposit(500)

secret_pass = input("enter the pin to check balance")
if secret_pass == "1234":
    icic_bank.if_you_are_auth(True)
else:
    icic_bank.if_you_are_auth(False)


secret_pass = input("enter the pin to withdrawl")
your_amount = int(input("enter the amount withdrawl"))
if secret_pass == "1234":
        icic_bank.if_you_are_auth_user(True, amount=your_amount)
        icic_bank.if_you_are_auth(flag=True)
else:
        icic_bank.if_you_are_auth_user(False)





