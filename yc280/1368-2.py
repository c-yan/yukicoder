def is_kadomatsu(a):
    if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        return False
    return min(a) == a[1] or max(a) == a[1]


def f(a):
    dp = [0] * (N + 1)
    for i in range(N + 1):
        if i != 0:
            dp[i] = max(dp[i], dp[i - 1])
        if i <= N - 3:
            if is_kadomatsu(a[i:i + 3]):
                dp[i + 3] = dp[i] + a[i]
    return dp[N]


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(max([f(A), f(A[1:N] + A[:1]), f(A[2:N] + A[:2])]))
