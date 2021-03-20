from math import log2

n, *A = map(int, open(0).read().split())

A.sort(reverse=True)

result = 0
for i in range(n):
    result += int(log2(i + 1)) * A[i]
print(result)
