p = str(bin(int(input())))
a = ''
c = 0


for i in range(len(p) - 1, 1, -1):
    a += p[i]

for i in range(len(a)-1, -1, -1):
    c += 2**(len(a)- i - 1) * int(a[i])
    
print(c)

