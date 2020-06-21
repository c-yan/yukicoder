N = int(input())
A = list(map(int, input().split()))

m = 1000000007

c = [[0] * N for _ in range(N)]
c[0][0] = 1
for i in range(1, N):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % m

result = 0
for i in range(N):
    result += c[N - 1][i] * A[i]
    result %= m
print(result)
