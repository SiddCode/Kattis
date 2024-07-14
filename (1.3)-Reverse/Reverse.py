u = int(input())

array = []
for i in range(u):
    p = input()
    array.append(p)

for i in range(u-1, -1, -1):
    print(array[i])