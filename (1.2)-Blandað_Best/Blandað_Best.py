u = int(input())

k = False
n = False


for i in range(u):
    a = input()
    if a == 'kjuklingur':
        k = True
    else:
        n = True

if k and n:
    print('blandad best')
elif k:
    print('kjuklingur')
else:
    print('nautakjot')