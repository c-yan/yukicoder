N, H, M, T = map(int, input().split())

a = H * 60 + M + (N - 1) * T
print(a // 60 % 24)
print(a % 60)
