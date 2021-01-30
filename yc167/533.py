m = 1000000007

N = int(input())

dp = [[0] * (max(4, N + 1)) for _ in range(4)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1
for i in range(1, N):
    if i + 3 <= N:
        dp[3][i + 3] += dp[1][i]
        dp[3][i + 3] += dp[2][i]
        dp[3][i + 3] %= m
    if i + 2 <= N:
        dp[2][i + 2] += dp[1][i]
        dp[2][i + 2] += dp[3][i]
        dp[2][i + 2] %= m
    if i + 1 <= N:
        dp[1][i + 1] += dp[2][i]
        dp[1][i + 1] += dp[3][i]
        dp[1][i + 1] %= m
print((dp[1][N] + dp[2][N] + dp[3][N]) % m)
