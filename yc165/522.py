N = int(input())

result = []
for a in range(1, N):
    for b in range(a, N):
        c = N - a - b
        if c < b:
            break
        result.append('%d %d %d' % (a, b, c))
print(*result, sep='\n')
