from itertools import permutations

K = int(input())

result = 0
for p in permutations('12345678'):
    if int(''.join(p)) % K == 0:
        result += 1
print(result)
