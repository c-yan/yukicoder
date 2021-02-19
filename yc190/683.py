A, B = map(int, input().split())


def f(X, Y):
    if X == 0 or Y == 0:
        return True
    if X < 0 or Y < 0:
        return False
    if X % 2 == 0:
        if f(X // 2, Y - 1):
            return True
    if Y % 2 == 0:
        if f(X - 1, Y // 2):
            return True
    return False


if f(A, B):
    print('Yes')
else:
    print('No')
