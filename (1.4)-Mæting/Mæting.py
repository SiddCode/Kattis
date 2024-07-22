a,b = map(int, input().split())

p = [int(x) for x in input().split()]
o = [int(x) for x in input().split()]
answer = ''

for i in range(len(p)):
        if p[i] in o:
                answer += str(p[i]) + ' '

print(answer)