# no return type and no parameter
# def say_hello():
#     print("hello")
#
#
# say_hello()


# no return type with argument
# def say_hello_args(name):
#     print("hello", name)
#
#
# result = say_hello_args("himanth")
# print(result)
#
#
# #no return tye and with default argument
# def say_hello_args_default(name="hemanth"):
#     print("hello", name)
#
# say_hello_args_default()
# say_hello_args_default("himanth")
# say_hello_args_default(name="sachin")


# with arguments + with return type

def sum_number_arguments_ret(a, b):
    return a + b


#result = sum_number_arguments_ret(3, 4)
#result = sum_number_arguments_ret(31, 43)
result = sum_number_arguments_ret(b=43, a=23)

print(result)
