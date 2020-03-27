S = input()

result = 1
for s in S:
    if s == 'L':
        result = result * 2
    elif s == 'R':
        result = result * 2 + 1
print(result)
