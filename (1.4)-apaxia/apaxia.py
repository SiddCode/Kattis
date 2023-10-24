u = input()

output = []
for i in u:
    if output:
        if output[-1] != i:
            output.append(i)
    else:
        output.append(i)
print("".join(output))