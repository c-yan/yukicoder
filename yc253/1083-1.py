N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)


def f(k, i):
    if i == N:
        return k
    result = -1
    for j in range(i, N):
        result = max(result, f(k % A[j], j + 1))
    return result


print(f(K, 0))
