S = input()

t = {'>': '<', '<': '>'}
print(''.join(t[c] for c in S[::-1]))
