N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

m = [[0] * N for _ in range(N)]

s1 = S.count(1)
t1 = T.count(1)
s2 = S.count(2)
t2 = T.count(2)

if s2 == 0 and t2 == 0:
    print(max(s1, t1))
elif s2 > 0 and t2 > 0:
    print(s2 * N + t2 * N - s2 * t2)
elif s2 == 0:
    print(t1 + t2 * N)
elif t2 == 0:
    print(s1 + s2 * N)
