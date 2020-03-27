L = int(input())
N = int(input())
W = list(map(int, input().split()))

W.sort()
t = 0
result = 0
for w in W:
    if t + w > L:
        break
    result += 1
    t += w
print(result)
