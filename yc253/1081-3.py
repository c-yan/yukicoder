N = int(input())
A = list(map(int, input().split()))

m = 1000000007

t = A[:]
for _ in range(N - 1):
    t = [(t[i] + t[i + 1]) % m for i in range(len(t) - 1)]
print(t[0])
