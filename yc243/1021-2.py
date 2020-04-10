N, M = map(int, input().split())
a = list(map(int, input().split()))
S = input()

p = 0
for c in S:
    if c == 'L':
        p = max(p - 1, -N + 1)
        if p < 0:
            a[-p] += a[-p - 1]
            a[-p - 1] = 0
    elif c == 'R':
        p = min(p + 1, N - 1)
        if p > 0:
            a[N - 1 - p] += a[N - p]
            a[N - p] = 0

if p > 0:
    print(*([0] * p + a)[:N])
elif p < 0:
    print(*(a + [0] * -p)[-p:N - p])
else:
    print(*a)
