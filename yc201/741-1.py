N = int(input())

m = 1000000007

result = 1
for i in range(9, 0, -1):
    result *= N + i
    result %= m
    result *= pow(i, -1, m)
    result %= m
print(result)
