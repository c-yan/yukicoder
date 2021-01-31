m = 1000000007

N = int(input())

result = 1
for i in range(1, N * 2 + 1):
    result *= i
    result %= m
result *= pow(pow(2, N, m), m - 2, m)
result %= m
print(result)
