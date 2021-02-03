from itertools import permutations

N, M = map(int, input().split())
scores = [tuple(map(int, input().split())) for _ in range(M)]

r = [0] * N
result = 0
for p in permutations(range(N)):
    for i in range(N):
        r[p[i]] = i
    t = 0
    for item1, item2, score in scores:
        if r[item1] < r[item2]:
            t += score
    result = max(result, t)
print(result)
