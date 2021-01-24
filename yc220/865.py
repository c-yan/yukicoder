N = int(input())
A = list(map(int, input().split()))

a = [0] * (N - 23)
a[0] = sum(A[:24])
for i in range(1, N - 23):
    a[i] = a[i - 1] - A[i - 1] + A[i + 23]

result = []
m = max(a)
Q = int(input())
for _ in range(Q):
    T, V = map(int, input().split())
    d = V - A[T - 1]
    A[T - 1] = V
    for i in range(max((T - 1) - 23, 0), min((T - 1) + 1, len(a))):
        a[i] += d
        m = max(m, a[i])
    result.append(m)
print(*result, sep='\n')
