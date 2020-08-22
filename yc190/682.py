A, B = map(int, input().split())

result = 0
for i in range(A, B + 1):
    if (A + B + i) % 3 == 0:
        result += 1
print(result)
