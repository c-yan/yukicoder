x, N, *a = map(int, open(0).read().split())

m = 1000003

result = 0
for n in a:
    result += pow(x, n, m)
    result %= m
print(result)
