a = [list(map(int, input().split())) for _ in range(4)]

used = {0}


def is_ok():
    b = a[0] + a[1] + a[2] + a[3]
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    return all(x == y for x, y in zip(b, c))

def pos_zero():
    for y in range(4):
        for x in range(4):
            if a[y][x] != 0:
                continue
            return y, x


def f():
    if is_ok():
        return True

    y, x = pos_zero()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue
        v = a[ny][nx]
        if v in used:
            continue
        used.add(v)
        a[y][x] = v
        a[ny][nx] = 0
        ret = f()
        if ret:
            return True
        a[y][x] = 0
        a[ny][nx] = v
        used.remove(v)
    return False


if f():
    print('Yes')
else:
    print('No')
