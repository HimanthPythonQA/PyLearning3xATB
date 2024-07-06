# recursion: its a programing technique where afunction calls itself in order to solve aproblem.
# it has a base case & recursive case
#
# find factorial of 5

def factorial_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_number(n - 1)


print(factorial_number(5))

# find the sum of number 12345 = 15
number = 12345
r = number % 10
q = number // 10
print(r)
print(q)

r1 = q % 10
q1 = q // 10
print(r1)
print(q1)

r2 = q1 % 10
q2 = q1 // 10
print(r2)
print(q2)

r3 = q2 % 10
q3 = q2 // 10
print(r3)
print(q3)

r4 = q3 % 10
q4 = q3 // 10
print(r4)
print(q4)

print(r + r1 + r2 + r3 + r4)


# find the sum of number 12345 = 15 in recursive form

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(12345))


def addision_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        n = n // 10
    return sum_digits

print(addision_of_digits(12345))
