u = int(input())
max = [0, '']
for i in range(u):
    user = input().split()
    if int(user[1]) > max[0]:
        max[0] = int(user[1])
        max[1] = user[0]

print(max[1])