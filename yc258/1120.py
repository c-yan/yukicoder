N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if N == 2:
    if sum(A) == sum(B):
        print(abs(A[0] - B[0]))
    else:
        print(-1)
elif N > 2:
    if sum(B) > sum(A):
        print(-1)
    elif (sum(A) - sum(B)) % (N - 2) == 0:
        t = (sum(A) - sum(B)) // (N - 2)
        s = 0
        for i in range(N):
            if A[i] - B[i] > t:
                print(-1)
                break
            if B[i] - A[i] > t:
                print(-1)
                break
            if (B[i] - (A[i] - t)) % 2 == 1:
                print(-1)
                break
            s += t - (A[i] - B[i])
        else:
            if s != 2 * t:
                print(-1)
            else:
                print(t)
    else:
        print(-1)
