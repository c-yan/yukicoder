N = int(input())

a = max(N - 10, 0)

result = a * 5
p = a
while p != N:
    if result % 5 in [0, 1, 2]:
        p += 1
    else:
        p -= 1
    result += 1
print(result)
