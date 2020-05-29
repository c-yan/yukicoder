n = int(input())

for i in range(10 ** 5, 0, -1):
    if n % (i * i) == 0:
        print(i, n // (i * i))
        break
