S = input()

result = []
for s in S:
    if s == 'I' or s == 'l':
        result.append('1')
    elif s == 'O' or s == 'o':
        result.append('0')
    else:
        result.append(s)
print(''.join(result))
