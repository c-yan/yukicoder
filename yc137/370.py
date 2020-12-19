N, M, *D = map(int, open(0).read().split())

D.sort()

result = 10 ** 20
for i in range(M - (N - 1)):
    if D[i] <= 0 and D[i + (N - 1)] <= 0:
        result = min(result, -D[i])
    elif D[i] <= 0 and D[i + (N - 1)] > 0:
        result = min(result, -D[i] * 2 + D[i + (N - 1)] * 1)
        result = min(result, -D[i] * 1 + D[i + (N - 1)] * 2)
    elif D[i] > 0 and D[i + (N - 1)] > 0:
        result = min(result, D[i + (N - 1)])
print(result)
