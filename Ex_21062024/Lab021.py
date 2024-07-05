# decorator: its an essential function which takes other function as argument & returns a new function
#

import time


# def my_decorator(func):
#     def wrapper():
#         print("starting...")
#         print("************")
#         func()
#         print("************")
#         print("ending...")
#
#     return wrapper()
#
# @my_decorator
# def say_hello():
#     print("say hello")


def note_time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("time taken" + str(end_time - start_time))

    return wrapper()

@note_time_decorator
def logs_function():
    time.sleep(5)
    print("print the logs of time taken")
