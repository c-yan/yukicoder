N, H, *T = map(int, open(0).read().split())

print(*[t + H for t in T])
