N, *a = map(int, open(0).read().split())

b = sum(a) // (N - 1)

tsuru = 0
kame = 0

for x in a:
    if b - x == 2:
        tsuru += 1
    elif b - x == 4:
        kame += 1
print(tsuru, kame)
