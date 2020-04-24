Q = int(input())

for i in range(Q):
    N, I, J = map(int, input().split())
    l = min(I, J, N - 1 - I, N - 1 - J)
    result = N * N - (N - 2 * l) * (N - 2 * l)
    N, I, J = N - 2 * l, I - l, J - l
    if I == 0:
        result += J
    elif J == N - 1:
        result += N - 1 + I
    elif I == N - 1:
        result += 2 * (N - 1) + (N - 1) - J
    elif J == 0:
        result += 3 * (N - 1) + (N - 1) - I
    print(result)
