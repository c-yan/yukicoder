a, b = map(int, input().split())

x = a
result = 0
t = 1 / 4096
while x < b:
    result += abs((x - a) * (x - b) * t)
    x += t
print(result)
