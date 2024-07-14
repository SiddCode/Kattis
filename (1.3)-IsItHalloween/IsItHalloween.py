u = input()

if (u[0:3] == 'OCT' and u[4:] == '31') or (u[0:3] == 'DEC' and u[4:] == '25'):
    print('yup')
else:
    print('nope')