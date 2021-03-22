V, T, P = map(int, input().split())

def f(t):
    return t - V * P - ((t - 1) // T + 1)

t = V * (P + 1)
while True:
    a = f(t)
    if a == V:
        break
    t += V - a
print(t)
