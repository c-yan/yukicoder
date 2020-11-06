from bisect import bisect_left

N, M, C = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
c = 0
for x in a:
    t = ((C + 1) + x - 1) // x
    i = bisect_left(b, t)
    c += M - i
print(c / (N * M))
