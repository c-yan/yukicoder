N = int(input())

m = 1000000007

dp = [0] * 10
dp[0] = 1
for _ in range(N):
    for i in range(8, -1, -1):
        for j in range(i + 1, 10):
            dp[j] += dp[i]
            dp[j] %= m
print(sum(dp) % m)
