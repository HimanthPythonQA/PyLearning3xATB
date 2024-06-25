global_a = 11


def f1():
    print("hello")
    print(global_a)


f1()


def outer_function():
    var1 = 30

    def inner_function():
       print("hii")
       print(var1)

    inner_function()

outer_function()


number = [1, 2, 3, 4]


def do_something(himanth_list):
    himanth_list.append(5)
    himanth_list[0] = 18
    return himanth_list

number.append(188)
l = do_something(number)
print(l)
