N, p = map(int, input().split())

m = 1000000007

a = [0] * max(N + 1, 3)
a[1] = 0
a[2] = 1
for i in range(3, N + 1):
    a[i] = (p * a[i - 1] + a[i - 2]) % m

c = [0] * (N + 1)
for i in range(1, N + 1):
    c[i] = (c[i - 1] + a[i]) % m

result = 0
for i in range(1, N + 1):
    result += a[i] * c[i]
    result %= m
print(result)
