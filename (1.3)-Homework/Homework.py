p = input().split(';')

s = 0
for i in range(len(p)):
    if '-' in p[i]:
        a = [int(x) for x in p[i].split('-')]
        s += a[1] - a[0] + 1
    else:
        s += 1

print(s)