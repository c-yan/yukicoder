A, B = map(int, input().split())

if A < B:
    print('YES')
else:
    print('NO')
print(abs((A + 1) - B))
