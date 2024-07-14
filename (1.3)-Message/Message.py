p = input().split()
word = ''
for i in range(int(p[0])):
    o = input()
    for j in range(int(p[1])):
        if o[j] != '.':
            word += o[j]

print(word)