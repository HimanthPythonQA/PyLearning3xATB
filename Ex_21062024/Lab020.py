# # set: it is collection of unique items e.g
list_of_items = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print(list_of_items)

list1 = [45.2, 22, 22, 39, 45]
set1 = set(list1)
print(set1)
print(len(set1))

q = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(q))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_test = set1.union(set2)
print(my_test)

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
my_new_set = set3.intersection(set4)
print(my_new_set)
my_new_set = set3.difference(set4)
print(my_new_set)
my_new_set = set4.difference(set3)
print(my_new_set)
subset = set4.issubset(set3)
print(subset)

set5 = {1, 2, 3, 4, 5, 6}
set6 = {3, 4, 5,}
subset1 = set6.issubset(set5)
print(subset1)

set_q = {"the_testing_academy", "for", "the_testing_academy."}
print(len(set_q))

for i in set_q:
    print(i)

set7 = {1,2,3,4,5,6,7,8,9,10,11,12}
print(len(set7))
set7.remove(10)
print(set7)
print(len(set7))
set7.add(100)
print(set7)
print(len(set7))
set7.pop()
print(set7)



def complete_in_future():
    pass

complete_in_future()
