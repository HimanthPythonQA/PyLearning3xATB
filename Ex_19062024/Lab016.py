def double_my_salary(salary):
    return salary * 2


new_salary = double_my_salary(100)
print(new_salary)
# lambda expression is used to do task in one line e.g

F_twice_salary = lambda salary: salary * 2
print(F_twice_salary(100))


def sum_three_nos(a, b, c):
    return a + b + c


o = sum_three_nos(9, 7, 90)
print(o)

j_sum3_numbers = lambda a, b, c: a + b + c
print(j_sum3_numbers(11, 88, 77))


def find_odd_even(num):
    if num % 2 == 0:
        print("even no")
    else:
        print("odd no")


find_odd_even(121)

check_odd_even = lambda num: "even" if num % 2 == 0 else "odd"
print(check_odd_even(22))

power_function = lambda: int(input("enter the num")) ** 3
f = power_function()
print(f)
