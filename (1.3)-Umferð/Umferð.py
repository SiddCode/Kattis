m = int(input())
n = int(input())
count = 0
for i in range(n):
    u = input()
    for j in range(m):
        if u[j] == '.':
            count += 1

print(count / (m*n))