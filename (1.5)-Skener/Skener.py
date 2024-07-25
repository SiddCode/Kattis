a,b,c,d = map(int, input().split())
matrix = []
for i in range(a):
    matrix.append(input())

for i in range(len(matrix)):
    string = ''
    for j in range(len(matrix[i])):
        string += matrix[i][j] * d 
    matrix[i] = string
    for k in range(c):
        print((matrix[i]))