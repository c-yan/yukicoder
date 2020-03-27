N = int(input())
M = int(input())

for _ in range(M):
    P, Q = map(int, input().split())
    if P == N:
        N = Q
    elif Q == N:
        N = P
print(N)
