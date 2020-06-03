P1 = int(input())
P2 = int(input())
N = int(input())

t = set()
result = 0
for _ in range(N):
    R = int(input())
    if R in t:
        result += P1 + P2
    else:
        t.add(R)
print(result)
