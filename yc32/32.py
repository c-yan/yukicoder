L = int(input())
M = int(input())
N = int(input())

M += N // 25
N %= 25
L += M // 4
M %= 4
L %= 10
print(L + M + N)
