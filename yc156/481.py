B = list(map(int, input().split()))

print(list(set(i for i in range(1, 11)) - set(B))[0])
