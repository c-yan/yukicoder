N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
print(A[0] + sum([a for a in A[1:] if a > 0][:K - 1]))
