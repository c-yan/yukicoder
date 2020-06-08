N = int(input())
S = input().split()
T = input().split()

for i in range(N):
    if S[i] != T[i]:
        print(i + 1)
        print(S[i])
        print(T[i])
        break
