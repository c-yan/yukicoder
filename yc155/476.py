n, a = map(int, input().split())
x = list(map(int, input().split()))

if sum(x) == a * n:
    print('YES')
else:
    print('NO')
