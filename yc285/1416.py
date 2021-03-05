n, *A = map(int, open(0).read().split())

A.sort(reverse=True)

result = 0
i = 0
for k in range(100):
    for j in range(2 ** k):
        result += k * A[i]
        i += 1
        if i == n:
            break
    if i == n:
        break
print(result)
