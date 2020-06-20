# PyPy でのみ AC
T = input()
D = int(input())

m = 1000000007


def update(t, nt, v):
    for i in range(10):
        ni = i + v
        if ni > 9:
            ni -= 9
        nt[ni] += t[i]
        nt[ni] %= m


t = [0] * 10
t[0] = 1
for c in T:
    nt = [0] * 10
    if c != '?':
        update(t, nt, int(c))
    else:
        for i in range(10):
            update(t, nt, i)
    t = nt
print(t[D])
