N, M, P, Q = map(int, input().split())

result = (N // (M * (12 + Q))) * 12
N %= M * (12 + Q)
if N <= M * (P - 1):
    result += (N + (M - 1)) // M
else:
    result += P - 1
    N -= M * (P - 1)
    if N <= 2 * M * Q:
        result += (N + (2 * M - 1)) // (2 * M)
    else:
        result += Q
        N -= 2 * M * Q
        result += (N + (M - 1)) // M
print(result)
