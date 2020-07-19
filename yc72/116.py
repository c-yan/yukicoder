N, *A = map(int, open(0).read().split())

def is_kadomatsu(A, B, C):
    if A == B or B == C or A == C:
        return False
    t = sorted([A, B, C])[1]
    return t == A or t == C

result = 0
for i in range(N - 2):
    if is_kadomatsu(A[i], A[i + 1], A[i + 2]):
        result += 1
print(result)
