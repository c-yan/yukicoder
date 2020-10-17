W = int(input())
D = int(input())

for i in range(D - 1):
    t = int(W / ((D - i) * (D - i)))
    W -= t
print(W)
