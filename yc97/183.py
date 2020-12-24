N, *A = map(int, open(0).read().split())

result = {0}
for a in set(A):
    for b in list(result):
        result.add(a ^ b)
print(len(result))
