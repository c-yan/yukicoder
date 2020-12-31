from collections import Counter

N, X, *a = map(int, open(0).read().split())

c = Counter(a)
result = 0
for i in range(N):
    result += c[X - a[i]]
print(result)
