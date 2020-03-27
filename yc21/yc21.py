N = int(input())
K = int(input())
n = [int(input()) for _ in range(N)]

n.sort()
print(n[-1] - n[0])
