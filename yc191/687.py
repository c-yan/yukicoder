N = int(input())

for i in range(1, 10 + 1):
    if 1 <= N - i <= 10:
        print(i, N - i)
        exit()
