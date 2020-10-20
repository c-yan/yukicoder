from bisect import bisect_left

N, M, K = map(int, input().split())

s = {0}
for _ in range(N):
    A = list(map(int, input().split()))
    ns = set()
    for x in s:
        for a in A:
            if x + a > K:
                continue
            ns.add(x + a)
    s = ns

if len(s) == 0:
    print(-1)
else:
    print(K - max(s))
