N = int(input())
x = list(map(int, input().split()))

x.sort()
t = x[1] - x[0]

if t == 0:
    print('NO')
    exit()

for i in range(1, N - 1):
    if x[i + 1] - x[i] != t:
        break
else:
    print('YES')
    exit()
print('NO')
