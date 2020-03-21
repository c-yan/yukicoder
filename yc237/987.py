from operator import add, mul

N, M = map(int, input().split())
op, *B = input().split()
A = [int(input()) for _ in range(N)]

B = list(map(int, B))
if op == '+':
    op = add
elif op == '*':
    op = mul

for a in A:
    print(' '.join(str(op(a, b)) for b in B))
