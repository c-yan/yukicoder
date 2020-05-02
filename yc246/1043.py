# PyPy でのみ AC
N, M = map(int, input().split())
V = list(map(int, input().split()))
R = list(map(int, input().split()))
A, B = map(int, input().split())

vt = {}
vt[0] = 1
for v in V:
    nvt = vt.copy()
    for k in vt:
        nvt.setdefault(k + v, 0)
        nvt[k + v] += vt[k]
    vt = nvt
del vt[0]

rt = {}
rt[0] = 1
for r in R:
    nrt = rt.copy()
    for k in rt:
        nrt.setdefault(k + r, 0)
        nrt[k + r] += rt[k]
    rt = nrt
del rt[0]

ra = [0] * (100000 + 1)
for k in rt:
    ra[k] = rt[k]

for i in range(1, 100000 + 1):
    ra[i] += ra[i - 1]

result = 0
for k in vt:
    rlow = (k + B - 1) // B - 1
    rhigh = k // A
    if rlow == -1:
        result += ra[rhigh] * vt[k]
    else:
        result += (ra[rhigh] - ra[rlow]) * vt[k]
    result %= 1000000007
print(result)
