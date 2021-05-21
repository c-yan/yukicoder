from sys import stdin

readline = stdin.readline

N = int(readline())
S = [readline()[:-1] for _ in range(N)]

dp = {'a': 0}
for s in sorted(S):
    if ''.join(sorted(s)) != s:
        continue
    start = s[0]
    last = s[-1]
    l = len(s)
    dp.setdefault(last, 0)
    for c in 'zyxwvutsrqponmlkjihgfedcba':
        if c not in dp:
            continue
        if start < c:
            continue
        dp[last] = max(dp[last], dp[c] + l)
print(max(dp.values()))
