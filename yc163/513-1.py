cache = {}
def query(x, y):
    if (x, y) in cache:
        return cache[x, y]
    print(x, y)
    result = int(input())
    cache[x, y] = result
    if result == 0:
        exit()
    return result


l = 0
r = 100000
while r - l >= 3:
    c1 = (l * 2 + r) // 3
    c2 = (l + r * 2) // 3
    if query(c1, 0) > query(c2, 0):
        l = c1
    else:
        r = c2

mv = query(l, 0)
mi = l
for j in range(l + 1, r + 1):
    if query(j, 0) >= mv:
        continue
    mv = query(j, 0)
    mi = j
AX = mi

AY = query(AX, 0)
query(AX, AY)
