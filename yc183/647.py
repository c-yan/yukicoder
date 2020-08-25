N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [tuple(map(int, input().split())) for _ in range(M)]

c = [0] * M
for a, b in AB:
    for i in range(M):
        x, y = XY[i]
        if x <= a and y >= b:
            c[i] += 1

m = max(c)
if m == 0:
    print(0)
else:
    print(*(i + 1 for i in range(M) if c[i] == m), sep='\n')
