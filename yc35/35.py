N = int(input())

x, y = 0, 0
for _ in range(N):
    T, S = input().split()
    T = int(T)
    x += min(int(12 * T / 1000), len(S))
    y += max(len(S) - int(12 * T / 1000), 0)
print(x, y)
