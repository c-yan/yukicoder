N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

c = 0
def f(k, i):
    global c
    if i == N:
        return k
    result = -1
    for j in range(i, N):
        c += 1
        result = max(result, f(k % A[j], j + 1))
    return result


print(f(K, 0))
print(c)
