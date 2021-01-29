def is_kadomatsu(a, b, c):
    if a == b or b == c or a == c:
        return False
    return min([a, b, c]) == b or max([a, b, c]) == b


def solve():
    dp = [0] * (N + 1)
    for i in range(N + 1):
        if i != 0:
            dp[i] = max(dp[i], dp[i - 1])
        if i <= N - 3:
            if is_kadomatsu(A[i], A[i + 1], A[i + 2]):
                dp[i + 3] = dp[i] + A[i]
    result = dp[N]
    if is_kadomatsu(A[N - 1], A[0], A[1]):
        dp = [0] * (N + 1)
        dp[2] = A[N - 1]
        for i in range(2, N + 1):
            dp[i] = max(dp[i], dp[i - 1])
            if i <= N - 4:
                if is_kadomatsu(A[i], A[i + 1], A[i + 2]):
                    dp[i + 3] = dp[i] + A[i]
        result = max(result, dp[N])
    if is_kadomatsu(A[N - 2], A[N - 1], A[0]):
        dp = [0] * (N + 1)
        dp[1] = A[N - 2]
        for i in range(1, N + 1):
            dp[i] = max(dp[i], dp[i - 1])
            if i <= N - 5:
                if is_kadomatsu(A[i], A[i + 1], A[i + 2]):
                    dp[i + 3] = dp[i] + A[i]
        result = max(result, dp[N])
    return result


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve())
