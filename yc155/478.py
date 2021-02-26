n, k = map(int, input().split())

result = ([1, 2, 0, 3] * ((n + 3) // 4))[:n]
for i in range(k):
    result[i] = result[k]
print(*result)
