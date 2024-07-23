word,a,b,answer = input(), int(input()), int(input()), int(input())

normal = a-b
absolute = abs(a-b)

if normal == answer and absolute == answer:
    print('VEIT EKKI')
elif normal == answer:
    print('JEDI')
else:
    print('SITH')