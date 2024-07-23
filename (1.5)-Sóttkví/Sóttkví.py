a,b,c = map(int, input().split())
count = 0
for i in range(a):
    if (int(input()) + 14) <= (b+c):
        count += 1

print(count)