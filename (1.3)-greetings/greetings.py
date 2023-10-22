user_input = input()
count_e = 0

if user_input[0] == 'h' and user_input[1] == 'e' and user_input[-1] == 'y' and user_input[-2] == 'e':
    for i in user_input:
        if i == 'e':
            count_e += 1

str_e = 'e' * count_e * 2

print('h' + str_e + 'y')