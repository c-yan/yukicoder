N = int(input())

m = 1000000007

dp = [0] * 10
dp[0] = 1
for _ in range(N):
    t = [0] * 10
    for i in range(10):
        for j in range(i, 10):
            t[j] += dp[i]
            t[j] %= m
    dp = t
print(sum(dp) % m)
