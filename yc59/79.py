N = int(input())
L = list(map(int, input().split()))

t = [0] * (6 + 1)
for l in L:
    t[l] += 1

m = max(t)
print(max(i for i in range(1, 6 + 1) if t[i] == m))
