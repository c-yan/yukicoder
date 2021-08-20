from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def is_movable(n):
    if A[n] == B[n]:
        return False
    elif A[n] < B[n]:
        if n == N - 1:
            return True
        else:
            return B[n] < A[n + 1]
    elif A[n] > B[n]:
        if n == 0:
            return True
        else:
            return B[n] > A[n - 1]

result = []
q = deque(range(N))
while q:
    i = q.popleft()
    if not is_movable(i):
        continue

    if A[i] < B[i]:
        moves = B[i] - A[i]
        dir = 'R'
    elif A[i] > B[i]:
        moves = A[i] - B[i]
        dir = 'L'

    for _ in range(moves):
        result.append('%d %s' % (i + 1, dir))

    A[i] = B[i]

    if i != 0:
        q.append(i - 1)
    if i != N - 1:
        q.append(i + 1)

print(len(result))
print(*result, sep='\n')
