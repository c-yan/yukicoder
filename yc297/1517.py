d = int(input())
a, b = map(int, input().split())

result = 10 ** 15
for i in range(d + 1):
    result = min(result, i * a + (d - i) * b)
print(result)
