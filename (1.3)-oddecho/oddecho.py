u = int(input())
a = []

for i in range(u):
    word_input = input()
    if i % 2 == 0:
        a.append(word_input)

for word in a:
    print(word)