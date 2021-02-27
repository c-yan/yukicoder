h, w = map(int, input().split())
sx, sy, gx, gy = map(lambda x: int(x) - 1, input().split())
b = [list(map(int, input())) for _ in range(h)]

movable = [[False] * w for _ in range(h)]
movable[sx][sy] = True
q = [(sx, sy)]
while q:
    x, y = q.pop()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if movable[nx][ny]:
            continue
        if abs(b[nx][ny] - b[x][y]) > 1:
            continue
        movable[nx][ny] = True
        q.append((nx, ny))
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        nx, ny = x + dx, y + dy
        mx, my = x + dx // 2, y + dy // 2
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if movable[nx][ny]:
            continue
        if b[nx][ny] != b[x][y]:
            continue
        if b[mx][my] >= b[x][y]:
            continue
        movable[nx][ny] = True
        q.append((nx, ny))
if movable[gx][gy]:
    print('YES')
else:
    print('NO')
