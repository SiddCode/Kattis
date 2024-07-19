a,b = map(int, input().split())

r = 0
for i in range(b):
    r += int(input())

print((r + (a-b) * -3)/a, (r + (a-b)*3)/a)