N = int(input())

t = [0] * (10 + 1)
for _ in range(N):
    for i in map(int, input().split()):
        t[i] += 1

result = 0
result += sum(t[i] // 2 for i in range(1, 10 + 1))
result += sum(t[i] % 2 for i in range(1, 10 + 1)) // 4
print(result)
