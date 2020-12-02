N, D = map(int, input().split())

T, K = map(int, input().split())
a = T
b = K - D

for _ in range(N - 1):
    T, K = map(int, input().split())
    c = max(a, b - D) + T
    d = max(a - D, b) + K
    a, b = c, d
print(max(a, b))
