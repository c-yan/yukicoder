N = int(input())

result = []
for i in range(0, N + 1):
    for j in range(0, N + 1):
        result.append((2 ** i) * (5 ** j))
result.sort()
print(*result, sep='\n')
