m = 1000000007

N = int(input())

if N == 0:
    print(1)
elif N == 1:
    print(12)
elif N == 2:
    print(65)
else:
    print((N * (17 * N + 6) + 1) % m)
