H, W, N, K = map(int, input().split())

if N == K:
    t = 0
else:
    t = K

if H * W % N == t:
    print('YES')
else:
    print('NO')
