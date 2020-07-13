N = int(input())

X, Y = map(int, input().split())
result = Y - X

if result <= 0:
    print(-1)
    exit()

for _ in range(N - 1):
    X, Y = map(int, input().split())
    if Y - X != result:
        print(-1)
        break
else:
    print(result)
