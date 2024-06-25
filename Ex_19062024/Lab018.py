squares = [1, 4, 9, 16, 25]

if not squares:
    print("not empty")

else:
    print("empty")


list = [1, 2, 3, 4, 5, 6]
# double the values in list
tem_list = []
for i in list:
    tem_list.append(i*2)
print(tem_list)


my_list = [1, 2, 3, 4, 5]
def double_item(i):
    return i*2
double_items = lambda i:i*2

double_list = list(map(lambda i: i * 2, my_list))
print(double_list)

print(list(map(lambda i: i * 2, my_list)))
print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))
