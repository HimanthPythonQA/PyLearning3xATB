# task1
# 1.
# The (Assignment operator) = operator is used to assign a value to a variable.
# Example x = 10
#  The (Equality comparison)== operator is used to compare two values to check if they are equal.
# Example : if x == 10:
#     print("x is 10")
# Does not change any values; it simply returns True or False based on the comparison.

# In Python, the ** operator is used for exponentiation. It raises the number on its left to the power of the number on its right.
# example
result = 5 ** 2
print(result)

# In Python, the ^ operator is used for bitwise XOR (exclusive OR) operations.
# This operator performs an XOR operation between the binary representations of two integers.
# It compares each bit of the numbers and returns a new integer
# where each bit is set to 1 if only one of the corresponding bits in the operands is 1 (but not both).
# example
result = 5 ^ 3
print(result)

# 2.
a = 2
Result_1 = (a ** 2)
Result_2 = (a ** 3)
print(Result_1, Result_2)

i = input("take input of i from user")
j = input("take input of j from user")
if i > j:
    print(i + " i is greater than j")
elif j==i:
    print(j + " j is equals to i")
else:
    print(j + " j is greater than i")
