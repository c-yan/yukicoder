from bisect import bisect_left

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
t0 = []
t1 = []
result = 0
for i in range(N):
    result += bisect_left(t0, a[i])
    t1.append(b[i])
    t1.sort()
    result += bisect_left(t1, a[i])
    if len(t1) == 300:
        t0.extend(t1)
        t0.sort()
        t1.clear()
print(result)
