p = int(input())

for i in range(p):
    count = 0
    a = [int(x) for x in input().split()]
    for i in range(0, len(a)-2, 1):
        if a[i] * 2 < a[i+1]:
            count += a[i+1] - 2*a[i]
    print(count)