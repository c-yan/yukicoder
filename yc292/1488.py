from sys import stdin

readline = stdin.readline

N, K = map(int, readline().split())
links = [{} for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, readline().split())
    a, b = a - 1, b - 1
    links[a][b] = c
    links[b][a] = c


def dfs(parent):
    l = links[parent]
    if len(l) == 0:
        return (0, 1)

    total_score = 0
    total_leaves = 0
    for child in l:
        del links[child][parent]
        score, leaves = dfs(child)
        total_score += score
        total_leaves += leaves
        t.append((l[child], leaves))
        total_score += l[child] * leaves
    return total_score, total_leaves


t = []
result, _ = dfs(0)

dp = [-1] * (K + 1)
dp[0] = 0
for i in range(len(t)):
    for j in range(K - 1,  -1, -1):
        if dp[j] == -1:
            continue
        a = j + t[i][0]
        if a > K:
            continue
        dp[a] = max(dp[a], dp[j] + t[i][0] * t[i][1])
result += max(dp)
print(result)
