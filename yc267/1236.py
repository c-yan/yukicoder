from bisect import bisect_left

A, B = map(int, input().split())

x = [i * 12 * 60 * 60 // 11 for i in range(12)]
t = (A * 60 + B) % (12 * 60) * 60
print(x[bisect_left(x, t)] - t)
