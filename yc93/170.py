from itertools import permutations

S = input()

print(len(set(''.join(p) for p in permutations(S))) - 1)
