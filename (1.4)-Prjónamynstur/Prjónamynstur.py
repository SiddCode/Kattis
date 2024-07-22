a,b = map(int, input().split())

sum = 0

for i in range(a):
    a = list(input())
    for j in range(len(a)):
        if a[j] == '.':
            sum += 20
        elif a[j] == 'O':
            sum += 10
        elif a[j] == '/':
            sum += 25
        elif a[j] == 'A':
            sum += 35
        elif a[j] == '^':
            sum += 5
        elif a[j] == 'v':
            sum += 22
        else:
            sum += 25

print(sum)