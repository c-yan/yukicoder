N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        if x1 == x2:
            result = max(result, len([None for x, y in XY if x == x1]))
            continue
        t = 0
        for k in range(N):
            x, y = XY[k]
            if abs((y2 - y1) / (x2 - x1) * (x - x1) + y1 - y) < 0.0001:
                t += 1
        result = max(result, t)
print(result)
