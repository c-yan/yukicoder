N = int(input())

x = 1
ng = set()
while x < 104127350297911241532841:
    ng.add(x)
    x *= 2

for a in range(1, min(100, N)):
    b = N - a
    if a in ng or b in ng:
        continue
    print(a, b)
    break
else:
    print(-1)
