s = open(0).read()
if len(s.split('\n')) < 4:
    print('"assert"')
    exit()
N, *A = map(int, s.split())
t = []
for i in range(3):
    for j in range(i + 1, 3):
        t.append(A[i] + A[j])
print(sorted({*t})[-2])
