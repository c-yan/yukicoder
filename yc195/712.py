N, M = map(int, input().split())

result = 0
for _ in range(N):
    A = input()
    result += A.count('W')
print(result)
