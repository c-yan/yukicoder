S = input()

result = 0
for c in S:
    if c == '0':
        result += 10
    else:
        result += int(c)
print(result)
