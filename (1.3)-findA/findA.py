u = input()
index_a = -1

for i in range(0, len(u)):
    if u[i] == 'a':
        index_a = i
        break

print(u[index_a:])