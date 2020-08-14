N = input()

for _ in range(99):
    N = sum(int(c) for c in str(N))
print(N)
