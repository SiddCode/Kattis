a,b,c = map(int, input().split())
d = [int(num) for num in input().split()]

print(int((a-b) * 0.9 - sum(d)))