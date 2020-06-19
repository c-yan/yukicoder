N = int(input())
A = list(map(int, input().split()))

m = 1000000007
l = 0
a = 1
b = 1
result = 1
for r in range(N):
    a *= A[r]
    b *= pow(A[r], r - l + 1, m)
    b %= m
    while a >= 1000000000:
        b *= pow(a, m - 2, m)
        a //= A[l]
        l += 1
    result *= b
    result %= m
print(result)
