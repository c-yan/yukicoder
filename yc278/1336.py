T = int(input())

m = 1000000007

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    t = 0
    for a in A:
        t = t * a + (t + a)
        t %= m
    print(t)
