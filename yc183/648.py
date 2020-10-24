n = int(input())

ok = 0
ng = 2000000000
while ng - ok > 1:
    m = (ok + ng) // 2
    if m * (m + 1) // 2 <= n:
        ok = m
    else:
        ng = m

if ok * (ok + 1) // 2 == n:
    print('YES')
    print(ok)
else:
    print('NO')
