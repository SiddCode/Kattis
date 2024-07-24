p = input()

for i in range(len(p)):
    if p[i] == ':' or p[i] == ';':
        if (i+1 < len(p) and p[i+1] == ')') or ( (i+2 < len(p)) and (p[i+1] == '-' and p[i+2] == ')')):
            print(i)