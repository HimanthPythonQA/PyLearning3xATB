my_list = [1, 2, 3, 4]
my_list1 = [1, True, "himanth", 11.11]

print("element at index 0:",my_list[2])

my_list[1] = 22
print("changing the value of element", my_list)

my_list.append(5)
print("appending value", my_list)

my_list.extend([6,7])
print("entending value",my_list)

my_list.insert(1,'a')
print("inserting value",my_list)

my_list.remove('a')
print("removing value",my_list)

my_copy_list = my_list.copy()
print(my_copy_list)

my_list.clear()
print("initial my list", my_list)
print(my_copy_list)

my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
print(my_copy_list[4])

