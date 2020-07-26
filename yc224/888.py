N = int(input())

result = 0
for i in range(1, int(N ** 0.5) + 1):
    if N % i != 0:
        continue
    result += i
    if N // i != i:
        result += N // i
print(result)
