import math

try:
    import math

    math.exp(1000)
except Exception as e:
    print(e)

try:
    a = int(input("enter the 1st num"))
    b = int(input("enter the 2nd num"))
    c = a / b
    print("result ", c)
except ValueError as e1:
    print(e1)
except ZeroDivisionError as e2:
    print(e2)
else:
    print("result is ", c)
finally:
    print("i will be executed anyhow")
