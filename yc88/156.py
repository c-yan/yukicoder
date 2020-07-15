N, M, *C = map(int, open(0).read().split())

C.sort()
for i in range(N):
    M -= C[i]
    if M <= 0:
        break

if M >= 0:
    print(i + 1)
elif M < 0:
    print(i)
