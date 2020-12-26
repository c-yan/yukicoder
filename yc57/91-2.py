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


for i in range(min(a), max(a) + 2):
    if is_ok(i):
        continue
    print(i - 1)
    break
