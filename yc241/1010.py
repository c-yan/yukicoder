x, y, h = map(int, input().split())

if x < y:
    x, y = y, x

x *= 1000
y *= 1000

result = 0

while y > h:
    x *= 2
    h *= 4
    result += 1

while x > h:
    y *= 2
    h *= 4
    result += 1

print(result)
