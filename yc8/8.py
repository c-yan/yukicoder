P = int(input())

for _ in range(P):
    N, K = map(int, input().split())
    if (N - 1) % (K + 1) == 0:
        print('Lose')
    else:
        print('Win')
