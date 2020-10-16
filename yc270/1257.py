A, B, C = map(int, input().split())
D, E, F = map(int, input().split())

if sorted([A, B, C]) == sorted([D, E, F]):
    print('Yes')
    print(2)
else:
    print('No')
