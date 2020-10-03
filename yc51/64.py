F0, F1, N = map(int, input(). split())

print([F0, F1, F0 ^ F1][N % 3])
