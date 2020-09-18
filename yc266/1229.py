N = int(input())

result = 0
for i in range(N // 5 + 1):
    for j in range(i + 1):
        for k in range(N // 3 + 1):
            if i * 5 + j * 2 + k * 3 == N:
                result += 1
print(result)
