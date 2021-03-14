N, K = map(int, input().split())

result = 1
for i in range(1, N + 1):
    if N % i != 0:
        continue
    if N // i < 2:
        continue
    result = max(result, i)
print(result)
