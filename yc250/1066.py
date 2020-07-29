# PyPy でのみ AC
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = 998244353

dp = [0] * (N + 1)
dp[1] = 1
dp[0] = A[0] - 1
for i in range(1, N):
    for j in range(i, -1, -1):
        dp[j + 1] += dp[j]
        dp[j + 1] %= m
        dp[j] *= A[i] - 1
        dp[j] %= m
print(*(dp[b] for b in B), sep='\n')
