N = int(input())

result = 0
for _ in range(N):
    H, M, h, m = map(int, input().replace(':', ' ').split())
    result += ((h * 60 + m) - (H * 60 + M) + (24 * 60)) % (24 * 60)
print(result)
