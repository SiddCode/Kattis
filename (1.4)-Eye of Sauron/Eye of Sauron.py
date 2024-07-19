p = input()
for i in range(len(p)):
    if p[i] == '(':
        left = i
    elif p[i] == ')':
        right = i


if (left == (len(p) - right - 1)):
    print('correct')
else:
    print('fix')