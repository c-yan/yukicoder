m = 1000000007

A, B, C = map(int, input().split())
K = int(input())

print(pow(A * B * C, pow(2, K, m - 1), m))
