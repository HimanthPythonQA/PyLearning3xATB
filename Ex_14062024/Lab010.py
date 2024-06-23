# printing odd numbers from 0 to 100
for i in range(1, 101, 2):
    print(i)

for j in range(30, 0, -1):
    print(j)

for j in reversed(range(0, 30)):
    print(j)

for counter in range(1, 101):
    print(counter)
    if counter == 5:
        break

print("outside the program")

for j in range(0, -30, -1):
    print(j)

for j in range(30):
    if j == 5 or j ==8 or j == 13:
        pass
    else:
        print(j)

for j in range(1, 30):
    if j % 3 != 0:
        print(j)
