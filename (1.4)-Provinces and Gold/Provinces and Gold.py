a,b,c = map(int, input().split())
p = 3*a + 2*b + c

if p >= 8:
    print('Province or Gold')
elif p >= 6:
    print('Duchy or Gold')
elif p == 5:
    print('Duchy or Silver')
elif p >= 3:
    print('Estate or Silver')
elif p == 2:
    print('Estate or Copper')
elif p >= 0:
    print('Copper')

