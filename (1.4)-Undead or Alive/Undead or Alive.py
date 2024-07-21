u = list(input())

smiley = False
unhappy = False

for i in range(len(u) - 1):
    if u[i] == ':':
        if u[i+1] == ')':
            smiley = True
        elif u[i+1] == '(':
            unhappy = True


if smiley and not unhappy:
    print('alive')
elif unhappy and not smiley:
    print('undead')
elif smiley and unhappy:
    print('double agent')
else:
    print('machine')