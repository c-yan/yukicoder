a, b = map(int, input().split())

if b - a > 0:
    print("+%d" % (b - a))
else:
    print(b - a)
