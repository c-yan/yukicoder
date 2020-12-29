X, Y = map(int, input().split())

s = {(0, 0)}
q = [(0, 0)]
for _ in range(3):
    nq = []
    while q:
        x, y = q.pop()
        for nx, ny in [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y - 2), (x - 1, y + 2),(x + 1, y - 2), (x + 1, y + 2), (x + 2, y - 1), (x + 2, y + 1)]:
            if (nx, ny) in s:
                continue
            s.add((nx, ny))
            nq.append((nx, ny))
    q = nq

if (X, Y) in s:
    print('YES')
else:
    print('NO')
