N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [a for a in A if a > 0]

if len(B) != 0:
    B.sort(reverse=True)
    print(sum(B[:K]))
else:
    B = [a for a in A if a <= 0]
    B.sort(reverse=True)
    print(B[0])
