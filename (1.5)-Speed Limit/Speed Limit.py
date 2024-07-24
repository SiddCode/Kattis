p = int(input())

while p != -1:
    total = 0
    prev = 0
    for i in range(p):
        a,b = map(int, input().split())
        total += a*(b-prev)
        prev = b
   
    print(total, 'miles')
    p = int(input())

