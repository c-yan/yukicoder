B, M, *C = map(int, open(0).read().split())


def ops(n):
    return sum(abs(c - n) for c in C)


l = min(C)
r = (sum(C) + B) // M
while r - l > 2:
    nl = (l * 2 + r) // 3
    nr = (l + r * 2 + 2) // 3
    if ops(nl) < ops(nr):
        r = nr
    else:
        l = nl
print(min(ops(n) for n in range(l, r + 1)))
