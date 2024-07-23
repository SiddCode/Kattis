a,b,c = int(input()), int(input()), int(input())

disc = b**2 - 4*a*c

if disc > 0:
    print(2)
elif disc == 0:
    print(1)
else:
    print(0)