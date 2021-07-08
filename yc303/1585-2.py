N = int(input())

ok = 0
ng = 10 ** 6 + 1
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if m ** 3 <= N:
        ok = m
    else:
        ng = m
if ok ** 3 == N:
    print('Yes')
else:
    print('No')
