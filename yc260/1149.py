N = int(input())

if N % 2 == 0:
    print(2, N // 2)
else:
    print(1, N // 2 + 1)

while True:
    t = int(input())
    if t in [0, 1]:
        exit()
    k, x = map(int, input().split())
    if t == 2:
        exit()
    print(k, N - (x - 1) - (k - 1))
