a = []
for i in range(10):
    p = int(input()) % 42
    if p not in a:
        a.append(p)

print(len(a))
    