# take 2-numbers from input user and add it.
num1 = input("Enter the 1st number")
num2 = input("enter the 2nd number")
result = int(num1) + int(num2)
print(result)
print(type(result))
pi = 3.14
print(type(pi))
num3 = 10
num4 = 12
result = num4 / num3
print(result)
print(type(result))
# r (raw string to print as it is)
dir = r'C:\nomedir\somedir'
print(dir)
# (f) formating: it will replace the values of the variables of place holders
first_name = 'Dasari'
second_name = 'Himanth'
print(first_name + ' ' + second_name)
print(first_name, second_name)
# (f) formating: it will replace the values of the variables of place holders
print(f'your full name is {first_name} {second_name}')
num = 5
print(f'{num}*1 = {num}')
print(f'{num}*2 = {num * 2}')
print(f'{num}*3 = {num * 3}')
print(f'{num}*4 = {num * 4}')
print(f'{num}*5 = {num * 5}')
# function id() is memory address where it is stored
name = 'himanth'
print(name)
print(type(name))
print(id(type(name)))
# function len() helps to find the length of string. it stars with 1
print(len(name))
# count() this function gives count of alphabets
a = name.count('h')
print(a)
print(name[4])
# for printing the index from left to right we can use -1
print(name[-4])
# function none() it has no valu, no return tpe, it is just used to initialize a value
name = None
print(name)
print(type(name))
shopping_list = ['milk', 'butter', "guava", "apple", "ghee"]
print(shopping_list)
print(type(shopping_list))
# Append this function add items to list at end
shopping_list.append("curd")
print(shopping_list)
# extend function helps to put more items in list
shopping_list.extend(["salt", "sugar"])
print(shopping_list)
# remove function helps to remove items in list
shopping_list.remove("salt")
print(shopping_list)
# pop function helps to remove last items in list and show in console
shopping_list.pop()
print(shopping_list)
print(shopping_list.index("milk"))
shopping_list[0] = "himanth"
print(shopping_list)
shopping_list.sort()
print(shopping_list)
# set() function help us to store unique items.
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)


