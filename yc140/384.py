H, W, N, K = map(int, input().split())

a = (H + W - 1) % N
if a == 0:
    a = N

if a == K:
    print('YES')
else:
    print('NO')
