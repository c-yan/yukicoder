H, N = map(int, input().split())
h = [int(input()) for _ in range(N - 1)]

h.append(H)
h.sort(reverse=True)
for i in range(N):
    if h[i] == H:
        t = i + 1
        break

if t % 10 == 1:
    print('%dst' % t)
elif t % 10 == 2:
    print('%dnd' % t)
elif t % 10 == 3:
    print('%drd' % t)
else:
    print('%dth' % t)
