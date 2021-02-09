from collections import Counter

N = int(input())

seats = [None] * 20
for _ in range(N):
    U = input()
    if U[0] == '0':
        _, n, m, *A = U.split()
        seats[int(n) - 1] = Counter(A)
    elif U[0] == '1':
        _, B = U.split()
        for i in range(20):
            if seats[i] is None:
                continue
            if B not in seats[i]:
                continue
            print(i + 1)
            seats[i][B] -= 1
            if seats[i][B] == 0:
                del seats[i][B]
            break
        else:
            print(-1)
    elif U[0] == '2':
        _, C = U.split()
        seats[int(C) - 1] = None
