x, y, r = map(int, input().split())

print(abs(x) + abs(y) + int(2 ** 0.5 * r + 1))
