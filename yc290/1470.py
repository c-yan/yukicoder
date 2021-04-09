from collections import Counter

N, *A = map(int, open(0).read().split())

c = Counter(A)

result = 0
if 1 in c:
    a = c[1]
else:
    a = 0
if 2 in c:
    b = c[2]
else:
    b = 0
result += a * b * 3
c = N - a - b
result += c * a * 2
result += c * b
print(result)
