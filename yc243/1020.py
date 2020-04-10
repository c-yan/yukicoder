N, K = map(int, input().split())
S = input()

if (N - K) % 2 == 0:
    print(S[K-1:] + S[:K-1][::-1])
else:
    print(S[K-1:] + S[:K-1])
