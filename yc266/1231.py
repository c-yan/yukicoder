N, *A = map(int, open(0).read().split())

dp = [-1] * 10
dp[0] = 0
for a in A:
    t = [-1] * 10
    for i in range(10):
        if dp[i] == -1:
            continue
        if t[i] < dp[i]:
            t[i] = dp[i]
        n = (i + a) % 10
        if t[n] < dp[i] + 1:
            t[n] = dp[i] + 1
    dp = t
print(dp[0])
