N = int(input())

a0 = int(input())
t = 1
print(t)
for _ in range(N - 1):
    a = int(input())
    if a > a0:
        t += 1
    print(t)
