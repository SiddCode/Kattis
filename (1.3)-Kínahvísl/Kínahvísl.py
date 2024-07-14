a,b = input(), input()
c = 1
for i in range(len(a)):
    if a[i] != b[i]:
        c+=1
print(c)