N, *A = map(int, open(0).read().split())

if N == 1:
    print(101)
    exit()

a = sum(A)
result = 0
for i in range(100 + 1):
    if (i + a) % N == 0:
        result += 1
print(result)
