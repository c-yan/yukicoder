N = int(input())
a = list(map(int, input().split()))

print(min(a[i + 1] - a[i] for i in range(N - 1)))
print(a[-1] - a[0])
