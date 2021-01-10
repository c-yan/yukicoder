N, K, *a = map(int, open(0).read().split())

result = 0
for i in range(K):
    while True:
        swapped = False
        for j in range(0, N - i - K, K):
            if a[i + j] > a[i + j + K]:
                a[i + j], a[i + j + K] = a[i + j + K], a[i + j]
                result += 1
                swapped = True
        if not swapped:
            break

if all(x == y for x, y in zip(a, sorted(a))):
    print(result)
else:
    print(-1)
