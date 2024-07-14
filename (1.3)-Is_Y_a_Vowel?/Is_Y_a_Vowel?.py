p = input().lower()
c = 0
c_y = 0
for i in range(len(p)):
    if p[i] == 'a' or p[i] == 'e' or p[i] == 'i' or p[i] == 'o' or p[i] == 'u':
        c += 1
    if p[i] == 'y':
        c_y += 1
 
print(str(c) + ' ' + str(c + c_y))