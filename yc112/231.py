N = int(input())
GD = [tuple(map(int, input().split())) for _ in range(N)]

a = [(GD[i][0] - 30000 * GD[i][1], i + 1) for i in range(N)]
a.sort(reverse=True)

for i in range(6):
    b = (a[:i] * 6)[:6]
    if sum(x for x, y in b) < 30000 * 100:
        continue
    print('YES')
    print(*(y for x, y in b), sep='\n')
    break
else:
    print('NO')
