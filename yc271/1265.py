N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

a = []
for i in range(N - 1):
    for j in range(i + 1, N):
        d = (xy[i][0] - xy[j][0]) * (xy[i][0] - xy[j][0]) + (xy[i][1] - xy[j][1]) * (xy[i][1] - xy[j][1])
        a.append((d, i, j))
a.sort()

result = 0
t = set()
for _, i, j in a:
    if i in t or j in t:
        continue
    if i == 0:
        result += 1
        t.add(j)
    else:
        t.add(i)
        t.add(j)
print(result)
