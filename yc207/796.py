N = int(input())

x = (3 + (N - 1)) % 3
if x == 0:
    print(*([3] + [1] * (N - 2) + [2]))
elif x == 1:
    print(*([3] + [1] * (N - 1)))
elif x == 2:
    print(*([3] + [1] * (N - 3) + [2, 2]))
