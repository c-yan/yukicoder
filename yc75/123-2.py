N, M, *A = map(int, open(0).read().split())

result = 1
for a in A[::-1]:
    if result == 1:
        result = a
    else:
        if a >= result:
            result -= 1
print(result)
