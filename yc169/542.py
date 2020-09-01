A, B = map(int, input().split())

result = set()
for a in range(A + 1):
    for b in range(B + 1):
        result.add(a + 5 * b)
result.remove(0)
print(*sorted(result), sep='\n')
