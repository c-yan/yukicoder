N, *p = map(int, open(0).read().split())

for x in p:
    if x == 2:
        print(2)
    else:
        print((x - 1) * (x - 1))
