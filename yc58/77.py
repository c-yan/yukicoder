N, *A = map(int, open(0).read().split())


def f(l):
    x = list(range(1, l // 2 + 1)) + [(l + 1) // 2] + list(range(l // 2, 1 - 1, -1))
    under = 0
    over = 0
    for i in range(min(l, N)):
        if x[i] >= A[i]:
            under += x[i] - A[i]
        else:
            over += A[i] - x[i]
    if l > N:
        under += sum(x[N:])
    elif l < N:
        over += sum(A[l:])
    return max(under, over)

a = int(sum(A) ** 0.5 * 2 - 1)
if a % 2 == 0:
    a -= 1

result = 10 ** 18
for i in range(1, a + 1, 2):
    result = min(result, f(i))
print(result)
