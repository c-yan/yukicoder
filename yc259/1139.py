N, D = map(int, input().split())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

t = sum(v)
print((D + t - 1) // t)
