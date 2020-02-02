S = input()

result = 0
for c in S:
    if c in '0123456789':
        result += int(c)
print(result)
