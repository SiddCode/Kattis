p = input()


for i in range(3):
    a = [int(x) for x in input().split()]
    if 7 in a:
        continue
    else:
        print(0)
        exit()

print(777)