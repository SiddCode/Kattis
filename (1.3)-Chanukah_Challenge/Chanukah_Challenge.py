u = int(input())

for i in range(u):
    o = input().split()
    b = int(o[1])
    answer = (b+1)*(b+2)/2 -1
    print(o[0] + ' ' + str(round(answer)))