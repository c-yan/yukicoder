N, *d = map(int, open(0).read().split())

for i in range(N):
    if d[i] == 1:
        print(10)
    else:
        print('9' + '0' * (d[i] - 1))
