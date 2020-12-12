N = int(input())

result = []
for i in range(N):
    print('?', N - 1)
    print(*(j + 1 for j in range(N) if j != i))
    ans = int(input())
    if ans == 0:
        result.append(i + 1)

print('!', len(result))
print(*result)
