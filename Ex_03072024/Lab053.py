# how to make our own custom exception
class MyCustomException(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message)


balance = 100;
withdraw = int(input("enter the amount"))
if withdraw > balance:
    raise MyCustomException("bal is low")
else:
    print("Remain bal is",(balance-withdraw))
