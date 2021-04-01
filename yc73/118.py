from collections import Counter

m = 1000000007

N, *A = map(int, open(0).read().split())

d = list(Counter(A).values())
result = 0
for i in range(len(d) - 2):
    for j in range(i + 1, len(d) - 1):
        for k in range(j + 1, len(d)):
            result += d[i] * d[j] * d[k]
            result %= m
print(result)
