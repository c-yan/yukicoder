N, *A = map(int, open(0).read().split())

dp = [[-1] * 10 for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(10):
        if dp[i][j] == -1:
            continue
        dp[i + 1][(j + A[i]) % 10] = max(dp[i + 1][(j + A[i]) % 10], dp[i][j] + 1)
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
print(dp[N][0])
