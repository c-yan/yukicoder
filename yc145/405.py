S1, T = input().split()
T = int(T)

t = ['XII', 'I', 'II', 'III', 'IIII', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
print(t[(t.index(S1) + T) % 12])
