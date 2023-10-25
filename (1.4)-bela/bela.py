u = input()
sum = 0


dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}

non_dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}


for i in range(int(u[0]) * 4):
    card_input = input()
    if card_input[1] == u[2]:
        sum += dominant[card_input[0]]
    else:
        sum += non_dominant[card_input[0]]

print(sum)
