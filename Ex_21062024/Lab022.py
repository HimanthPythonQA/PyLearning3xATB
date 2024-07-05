# dictionary: it is a unordered collection of data which has keys and values. it is mutable in nature

my_dict1 = {"name" : "himanth", "age" : 31, "address" : "hyd"}
print(my_dict1)
print(len(my_dict1))
print(my_dict1["name"])
print(my_dict1["age"])
print(my_dict1["address"])
my_dict1["name"] = "hemanth"
print(my_dict1)


phone_book = dict(name="himanth", age=32, address="banglore")
print(phone_book)


himanth_details = \
    {"name":"hemanth", "age":31, "90":34.34, "ismale":True, "address":"AP"}
print(himanth_details.get("address"))
print(himanth_details["address"])
print(himanth_details.values())
print(himanth_details.keys())

my_dict2 = {'a':1, 'b':2, 'c':3, 'd':4, 'a':95, 'e':95,}
print(my_dict2)
print(len(my_dict2))
print(list(my_dict2.keys()))
print(list(my_dict2.values()))
for i in list(my_dict2.values()):
    print(i)

    for k,v in my_dict2.items():
        print(k,v)


from collections import OrderedDict
od = OrderedDict()
od['a'] = 45
od['c'] = 24
od['b'] = 96
od['d'] = 85
print(od)