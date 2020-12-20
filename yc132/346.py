S = input()

t = S.count('w')

result = 0
for c in S:
    if c == 'c':
        result += t * (t - 1) // 2
    elif c == 'w':
        t -= 1
print(result)
