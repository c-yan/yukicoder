k = int(input())

print(sum(1 / (n * (n + k)) for n in range(1, 10 ** 6)))
