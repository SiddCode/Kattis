o = int(input())

while True:
    p = [int(x) for x in str(o)]
    h = 0

    for i in range(len(p)):
        h += int(p[i])

    if o % h == 0:
        print(o)
        break
    o += 1