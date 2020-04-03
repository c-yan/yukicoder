N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))

A = [a + 1 for a in A]
A.sort(reverse=True)

for i in range(len(A)):
    if Z == 0:
        break
    if A[i] >= 10000:
        t = A[i] // 10000
        t = min(t, Z)
        Z -= t
        A[i] -= t * 10000
    else:
        break
A = [a for a in A if a > 0]
A.sort(reverse=True)
A = A[Z:]

for i in range(len(A)):
    if Y == 0:
        break
    if A[i] >= 5000:
        t = A[i] // 5000
        t = min(t, Y)
        Y -= t
        A[i] -= t * 5000
    else:
        break
A = [a for a in A if a > 0]
A.sort(reverse=True)
A = A[Y:]

for i in range(len(A)):
    t = (A[i] + 999) // 1000
    t = min(t, X)
    X -= t
    A[i] -= t * 1000
A = [a for a in A if a > 0]

if len(A) == 0:
    print('Yes')
else:
    print('No')
