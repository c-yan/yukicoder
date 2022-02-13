from bisect import bisect_left

N, D, *A = map(int, open(0).read().split())

t = sorted(A)

for a in A:
    print(bisect_left(t, a - D + 1))
