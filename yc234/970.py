N = int(input())
y = list(map(int, input().split()))

sy = sum(y)
print(*[sy - yi * (N - 1) for yi in y])
