from collections import deque
from sys import stdin

readline = stdin.readline

INF = 10 ** 18

n, m = map(int, readline().split())

links = [[] for _ in range(n)]
for _ in range(m):
    s, t, d = map(int, readline().split())
    s, t = s - 1, t - 1
    links[s].append((t, d))
    links[t].append((s, d))

q = deque([(0, INF)])
dp = [(-1, -1) for _ in range(n)]
dp[0] = (INF, 0)
while q:
    cp, mw = q.popleft()
    if dp[cp][0] > mw:
        continue
    for np, lw in links[cp]:
        w, s = dp[np]
        nw = min(mw, lw)
        if w >= nw:
            continue
        if w == nw:
            dp[np] = (nw, min(s, dp[cp][1] + 1))
        else:
            dp[np] = (nw, dp[cp][1] + 1)
        q.append((np, nw))
print(dp[n - 1][0], dp[n - 1][1])
