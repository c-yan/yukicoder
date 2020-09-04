n, z = map(int, input().split())

for x in range(1, z + 1):
    for y in range(x, z + 1):
        if x ** n + y ** n == z ** n:
            print('Yes')
            exit()
print('No')
