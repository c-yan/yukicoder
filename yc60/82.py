W, H, C = input().split()
W, H = int(W), int(H)

d = {'B': 'W', 'W': 'B'}
for i in range(H):
    if i % 2 == 0:
        c = C
    else:
        c = d[C]
    for _ in range(W):
        print(c, end="")
        c = d[c]
    print("")
