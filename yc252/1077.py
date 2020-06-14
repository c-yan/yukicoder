N = int(input())
Y = list(map(int, input().split()))

a = sorted(set(Y))
dp = [0] * len(a)

for i in range(N):
    t = float('inf')
    for j in range(len(a)):
        t = min(t, dp[j])
        dp[j] = t + abs(Y[i] - a[j])

print(min(dp))
