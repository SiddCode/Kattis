p = int(input())
count = 0
flights = []
for i in range(p):
    row = [int(o) for o in input().split()]
    for j in range(len(row)):
        if row[j] != -1:
            count += 1
            flights.append([i+1, j+1, row[j]])

print(count)

for i in range(len(flights)):
    print(flights[i][0], flights[i][1], flights[i][2])