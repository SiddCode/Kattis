a,b = map(int, input().split())

if a == 0 and b == 0:
    print('Not a moose')
elif a == b:
    print('Even', a+b)
else:
    if a > b:
        print('Odd', 2*a)
    else:
        print('Odd', 2*b)