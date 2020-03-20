# PyPy なら AC
N, d, K = map(int, input().split())

buf0 = [0] * (d * N + K + 1)
buf1 = [0] * (d * N + K + 1)
buf0[0] = 1

for i in range(N):
    t = 0
    for j in range(d):
        t += buf0[j]
        t %= 1000000007
        buf1[j] = t
    for j in range(d, (i + 1) * d):
        t -= buf0[j - d]
        t += buf0[j]
        t %= 1000000007
        buf1[j] = t
    buf0, buf1 = buf1, buf0

print(buf0[K - N])
