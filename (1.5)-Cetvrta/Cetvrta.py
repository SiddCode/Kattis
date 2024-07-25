(a,b), (c,d), (e,f) = map(int, input().split()), map(int, input().split()), map(int, input().split())

left = 0
right = 0
if a != c and a != e:
    left = a
elif c != a and c != e:
    left = c
else:
    left = e

if b != d and b != f:
    right = b
elif d != b and d != f:
    right = d
else:
    right = f

print(left,right)