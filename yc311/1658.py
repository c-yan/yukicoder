N, K = map(int, input().split())

result = [1] * N
result[0] = 2 * K
result[1] = 2 * K + N - 2
print(*result)
