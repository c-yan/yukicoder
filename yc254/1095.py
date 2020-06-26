from itertools import accumulate

INF = float('inf')

N, *A = map(int, open(0).read().split())

l = list(accumulate(A, min))
r = list(accumulate(A[::-1], min))[::-1]

result = INF

# 凸 タイプの門松列の場合
for i in range(1, N - 1):
    a = l[i - 1]
    b = A[i]
    c = r[i + 1]
    if a <= b and c <= b:
        result = min(result, a + b + c)

# 凹 タイプの門松列の場合
for i in range(1, N - 1):
    a = l[i - 1]
    b = A[i]
    c = r[i + 1]
    if b <= a and b <= c:
        result = min(result, a + b + c)

if result == INF:
    print(-1)
else:
    print(result)
