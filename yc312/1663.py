a, b, c, d, m = map(int, input().split())

result = 0
for x in range(a, b + 1):
    for y in range(c, d + 1):
        result = max(result, (x + y) % m)
print(result)
