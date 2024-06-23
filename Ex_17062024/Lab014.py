def f1(a, b, c):
    return a + b + c


# result = f1(3, 4, 5)
result = f1(a=9, b=10, c=11)
print(result)


def f1(a=2, b=5, c=44):
    return a + b + c


# result = f1(3, 4, 5)
result = f1(a=9, b=10)
result1 = f1(a=19, b=20)
result2 = f1(a=19, b=20, c=44)
print(result, result1, result2)


def print_argument(*args):
    for i in args:
        print(i, "\n")


print_argument("amit", "pramod", "himanth")

a = ["himanth", "ammm", "hhhh"]
for i in a:
    print(i)


    def make_pizza(*topings):
        print(topings)
        for i in topings:
            print(i)

himanth = make_pizza("tomato")
hemanth = make_pizza("olives", "sweet corn", "pineapple")
manoj = make_pizza("panner", "cheeze")


def prepare_pizza(*topings, bases):
    print(topings, bases)


himanth = prepare_pizza("tomato", "paneer", bases="small")
