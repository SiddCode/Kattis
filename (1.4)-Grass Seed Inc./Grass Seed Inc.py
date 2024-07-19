p = float(input())
o = int(input())
area = 0
for i in range(o):
        a,b = map(float,input().split())
        product = a*b
        area += product
    
print(area*p)
