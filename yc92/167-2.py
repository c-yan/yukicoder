N = input()
M = input()

if len(M) == 1 and int(M) == 0:
    print(1)
else:
    n = int(N[-1])
    m = int(M[-2:]) % 4 + 4
    print(pow(n, m, 10))
