ok = 1
ng = 10 ** 9 + 1
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    print('?', m)
    if int(input()) == 1:
        ok = m
    else:
        ng = m
print('!', ok)
