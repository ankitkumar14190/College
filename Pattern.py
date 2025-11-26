n = 5
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

num = 1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
        num = num+1
    print()