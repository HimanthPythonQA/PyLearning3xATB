import os
all_dir = os.listdir("/EX_JULY/Ex_05072024")
print(all_dir)
fd = os.open('Testdata.txt', os.O_RDWR)
os.write(fd,b'hello iam writing')
os.close(fd)

