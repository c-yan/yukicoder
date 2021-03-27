A, B, S = map(int, input().split())

if S == 1:
    print(abs(A - 1) + 1)
elif abs(B - S) < abs(A - S):
    a = abs(B - S) + (S - 1) + abs(A - 1) + 1
    if A != 0:
        b = abs(B - S) + abs(S - A) + A
    else:
        b = 10 ** 18
    print(min(a, b))
else:
    print(abs(A - S) + (S - 1) + 1)
