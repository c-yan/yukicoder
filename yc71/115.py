N, D, K = map(int, input().split())

a = [N - i for i in range(K)][::-1]
n = sum(a) - D
if n < 0:
    print(-1)
    exit()

for i in range(K):
    if n == 0:
        break
    t = min(n, a[i] - (i + 1))
    a[i] -= t
    n -= t

if n != 0:
    print(-1)
else:
    print(*a)
