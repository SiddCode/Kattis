u = input().split(' ')

a,b = u[0], u[1]

i = input().split(' ')


for j in range(len(i)):
    if b == i[j]:
        store = j + 1

if store == 1:
    print('fyrst')
elif store == 2:
    print('naestfyrst')
else:
    print(str(store),'fyrst')