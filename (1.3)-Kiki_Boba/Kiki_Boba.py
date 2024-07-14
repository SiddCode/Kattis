p = input()

c_k = 0
c_b = 0

for i in range(len(p)):
    if p[i] == 'b':
        c_b += 1
    if p[i] == 'k':
        c_k += 1


if c_k == c_b and c_k > 0:
    print('boki')
elif c_k == c_b:
    print('none')
elif c_k > c_b:
    print('kiki')
else:
    print('boba')