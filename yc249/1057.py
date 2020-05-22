A, B = map(int, input().split())

if A == B:
    print(2 * A - 1)
else:
    print(min(A, B) * 2)
