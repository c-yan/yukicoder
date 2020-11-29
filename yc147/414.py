M = int(input())

for i in range(2, int(M ** 0.5) + 1):
    if M % i == 0:
        print(i, M // i)
        break
else:
    print(1, M)
