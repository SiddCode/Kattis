p = input()

for i in range(len(p)):
    if int(p[i]) == (i+1):
        continue
    else:
        print(-1)
        exit()

print(len(p))