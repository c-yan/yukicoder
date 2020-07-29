N, K, X, Y = map(int, input().split())
A = list(map(int, input().split()))

B = [((a - 1) + K - 1) // K for a in A]
B.sort(reverse=True)

if Y <= X:
    print(Y * B[0])
    exit()
t = (Y + (X - 1)) // X - 1
if t < N:
    print(Y * B[t] + X * sum(B[i] - B[t] for i in range(t)))
else:
    print(X * sum(B[i] for i in range(N)))
