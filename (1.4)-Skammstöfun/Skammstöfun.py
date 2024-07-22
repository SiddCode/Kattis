p = input()
a = [x[0] for x in input().split()]

for i in range(len(a)-1, -1, -1):
    if a[i].islower():
        a.pop(i)

print(''.join(a))