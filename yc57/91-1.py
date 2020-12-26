R, G, B = map(int, input().split())

a = [R, G, B]


def is_ok(n):
    m = 0
    p = 0
    for x in a:
        if x - n >= 0:
            p += (x - n) // 2
        else:
            m += n - x
    return p >= m


ok = min(a)
ng = max(a) + 1
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
