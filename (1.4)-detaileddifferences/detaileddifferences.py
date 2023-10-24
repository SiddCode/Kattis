num_cases = int(input())

a = []
b = []
output = ''

for i in range(num_cases):
    a_input = input()
    b_input = input()

    a.append(a_input)
    b.append(b_input)

for i in range(num_cases):
    output = ''

    for j in range(len(a[i])):
        if a[i][j] == b[i][j]:
            output += '.'
        else:
            output += '*'

    print(a[i])
    print(b[i])
    print(output)
    print()
