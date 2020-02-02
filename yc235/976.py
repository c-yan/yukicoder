M = int(input())

result = 1
for _ in range(128):
    result *= 2
    result %= M
print(result)
