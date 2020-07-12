C = ''.join(open(0).read().split())

result = 0
t = 0
for c in C:
    if c == 'o':
        t += 1
    else:
        t = 0
    result = max(result, t)
print(result)
