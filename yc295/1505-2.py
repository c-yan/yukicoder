N = int(input())
A = input()

print((N + 1) * N // 2 - sum((len(s) + 1) * len(s) // 2 for s in A.replace(' ', '').split('0')))
