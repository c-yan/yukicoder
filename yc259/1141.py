readline = open(0).readline

H, W = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(H)]
Q = int(readline())

m = 1000000007

total = 1
rows = [1] * H
cols = [1] * W
total0 = 0
rows0 = [0] * H
cols0 = [0] * W
for i in range(H):
    for j in range(W):
        x = A[i][j]
        if x == 0:
            total0 += 1
            rows0[i] += 1
            cols0[j] += 1
        else:
            total *= x
            total %= m
            rows[i] *= x
            rows[i] %= m
            cols[j] *= x
            cols[j] %= m

result = []
for _ in range(Q):
    r, c = map(lambda x: int(x) - 1, readline().split())
    x = A[r][c]
    t = total0 - rows0[r] - cols0[c]
    if x == 0:
        t += 1
    if t > 0:
        result.append(0)
        continue
    t = total * pow(rows[r], -1, m) % m * pow(cols[c], -1, m) % m
    if x != 0:
        t *= x
        t %= m
    result.append(t)
print(*result, sep='\n')
