N, K, M = map(int, input().split())
P = list(map(int, input().split()))
E = list(map(int, input().split()))
A = list(map(int, input().split()))
H = list(map(int, input().split()))

P.sort()
E.sort()
A.sort()
H.sort()

result = 0
for x in zip(P, E, A, H):
    y = sorted(x)
    result += pow(y[-1] - y[0], K, M)
    result %= M
print(result)
