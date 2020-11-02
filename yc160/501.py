N, D = map(int, input().split())

if D <= N:
    print('A' * D + 'C' * (N - D))
else:
    print('A' * (2 * N - D) + 'B' * (D - N))
