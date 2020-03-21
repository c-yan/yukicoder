from bisect import bisect_left

N, M, K = map(int, input().split())
op, *B = input().split()
A = [int(input()) for _ in range(N)]

B = list(map(int, B))

B.sort()

result = 0
if op == '+':
    for a in A:
        result += M - bisect_left(B, K - a)
elif op == '*':
    for a in A:
        result += M - bisect_left(B, K / a)
print(result)
