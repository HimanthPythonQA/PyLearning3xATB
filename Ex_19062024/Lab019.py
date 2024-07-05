# tuple() tuples are immutable in nature. so we cant use append, add etc...

my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 22
print(my_tuple)

y = my_tuple.index(1)
print(y)

# conversion list to tuple
t1 = tuple(["himanth", "hemanth", "tagore"])
print(t1)
# del t1
# print(t1)


hero1 = ("batman", "bruce wayne")
hero2 = ("wonder woman", "diana prince")
new_tuple = (hero1, hero2)

print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][0])
print(new_tuple[1][1])

# unpacking of tuples
q, w, e = (45, 66, 98)
print(q)
print(w)
print(e)

# search in tuples
cities = ("los angeles", "london", "paris", "tokyo")
print("paris" in cities)
print("new delhi" in cities)

t = (11,22,33)
new_t = t + (10,)
print(new_t)
my_list = list(t)
print(my_list)
my_list.append(5)
print(my_list)
