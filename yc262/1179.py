a, b, c = map(int, input().split())

t = b * b - 4 * a * c
if t < 0:
    print('imaginary')
elif t == 0:
    print(-b / (2 * a))
else:
    t = t ** 0.5
    result = [(-b - t) / (2 * a), (-b + t) / (2 * a)]
    result.sort()
    print(*result)
