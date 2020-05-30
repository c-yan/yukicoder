a = list(map(int, input().split()))

result = 0
for N in a:
    if N % 15 == 0:
        result += 8
    elif N % 5 == 0:
        result += 4
    elif N % 3 == 0:
        result += 4
    else:
        result += len(str(N))
print(result)
