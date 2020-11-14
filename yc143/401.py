N = int(input())

result = [[0] * N for _ in range(N)]

i = 1
y, x = 0, 0
d = 6
while i <= N * N:
    result[y][x] = i
    if d == 6:
        if x == N - 1 or result[y][x + 1] != 0:
            d = 2
            y += 1
        else:
            x += 1
    elif d == 2:
        if y == N - 1 or result[y + 1][x] != 0:
            d = 4
            x -= 1
        else:
            y += 1
    elif d == 4:
        if x == 0 or result[y][x - 1] != 0:
            d = 8
            y -= 1
        else:
            x -= 1
    elif d == 8:
        if y == 0 or result[y - 1][x] != 0:
            d = 6
            x += 1
        else:
            y -= 1
    i += 1

for y in range(N):
    print(*('%03d' % i for i in result[y]))
