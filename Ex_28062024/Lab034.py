class Bank_account:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("your balance is", self.balance)


icic_bank = Bank_account()
print(icic_bank.balance)
icic_bank.deposit(200)
print(icic_bank.show_balance())
icic_bank.deposit(35)
print(icic_bank.show_balance())
icic_bank.withdrawl(44)
print(icic_bank.show_balance())
