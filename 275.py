N = int(input())
A = list(map(int, input().split()))

A.sort()
if N == 0:
    print(0)
elif N % 2 == 1:
    print(A[N // 2])
else:
    print(sum((A[N // 2 - 1: N // 2 + 1])) / 2)
