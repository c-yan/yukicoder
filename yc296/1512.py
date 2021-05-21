from sys import stdin

readline = stdin.readline

az = 'abcdefghijklmnopqrstuvwxyz'

N = int(readline())
S = [readline()[:-1] for _ in range(N)]

S.sort()

dp = {chr(ord('a') - 1): 0}

for l in S:
    if ''.join(sorted(l)) != l:
        continue
    start = l[0]
    last = l[-1]
    dp.setdefault(last, 0)
    for c in reversed(az):
        if c not in dp:
            continue
        if start < c:
            continue
        dp[last] = max(dp[last], dp[c] + len(l))
    dp[last] = max(dp[last], len(l))
print(max(dp.values()))
