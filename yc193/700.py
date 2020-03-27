n, m = map(int, input().split())

for _ in range(n):
    if input().find('LOVE') != -1:
        print('YES')
        exit()
print('NO')
