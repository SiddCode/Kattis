import math

u = int(input())

for i in range(u):
    int_input = int(input())
    factorial = str(math.factorial(int_input))
    print(factorial[-1])