L = list(map(int, input().split()))
RBY = list(map(int, input().split()))

L.sort()
RBY.sort(reverse=True)

result = 0
result += (L[0] + L[1]) * 2 * RBY[0]
result += (L[0] + L[2]) * 2 * RBY[1]
result += (L[1] + L[2]) * 2 * RBY[2]

print(result)
