p = input().split()
o = []

for i in range(len(p)):
    if p[i][0] not in [o[j][0] for j in range(len(o))]:
        o.append([p[i][0], 1])
    else:
        for j in range(len(o)):
            if p[i][0] == o[j][0]:
                o[j][1] += 1

max = 0
for i in range(len(o)):
    if o[i][1] > max:
        max = o[i][1]

print(max)