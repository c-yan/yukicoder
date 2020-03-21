N, M, K = map(int, input().split())
op, *B = input().split()
A = [int(input()) for _ in range(N)]

B = list(map(int, B))

result = 0
sb = sum(B) % K
if op == '+':
    for a in A:
        result += sb
        result %= K
        result += (a * M) % K
        result %= K
elif op == '*':
    for a in A:
        result += (a * sb) % K
        result %= K
print(result)
