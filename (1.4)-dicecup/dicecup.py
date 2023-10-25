
u = input()
int1 = ''
int2 = ''

for i in range(len(u)):
    if u[i] != ' ':
        int1 += u[i]
    else:
        int2 = u[i+1:]
        break

int1 = int(int1)
int2 = int(int2)

sum_array = [0] * (int1 + int2 - 1)

for i in range(1, int1 + 1):
    for j in range(1, int2 + 1):
        sum = i + j
        sum_array[sum - 2] += 1

maximum_value = max(sum_array)

for i in range(len(sum_array)):
    if sum_array[i] == maximum_value:
        print(i + 2)