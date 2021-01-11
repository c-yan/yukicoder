xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

print(((yb - ya) * xa + ya * (xa + xb)) / (xa + xb))
