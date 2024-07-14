p = input().lower()
c = 0
for i in range(len(p)):
    if 97 <= ord(p[i]) <= 122:
        c += 1

print(c)