N = int(input())

for i in range(int(N ** (1 / 3)) - 1, int(N ** (1 / 3)) + 1 + 1):
    if i ** 3 == N:
        print('Yes')
        break
else:
    print('No')
