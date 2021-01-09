N, *a = map(int, open(0).read().split())

result = N
for i in range(N):
    if a[N - 1 - i] == result:
        result -= 1
print(result)
