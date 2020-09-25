m = 1000000007

N, K, *A = map(int, open(0).read().split())

for i in range(N):
    A[i] -= K

dp = {}
dp[0] = 1
for a in A:
    for k in sorted(dp, reverse=True) if a >= 0 else sorted(dp):
        dp.setdefault(k + a, 0)
        dp[k + a] += dp[k]

dp[0] -= 1
print(sum(dp[k] for k in dp if k >= 0) % m)
