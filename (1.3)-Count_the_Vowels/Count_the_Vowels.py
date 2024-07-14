p = input().lower()
c = 0
for i in range(len(p)):
    if p[i] == 'a' or p[i] == 'e' or p[i] == 'i' or p[i] == 'o' or p[i] == 'u':
        c += 1

print(c)

