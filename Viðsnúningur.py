


user_input = input("")
string = ''

for i in range(len(user_input) - 1, -1, -1):
    string += user_input[i]

print(string)