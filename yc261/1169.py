N = int(input())

for i in range(1, N + 1):
    print(*((2 * i - j) % N if (2 * i - j) %
            N != 0 else N for j in range(1, N + 1)))
