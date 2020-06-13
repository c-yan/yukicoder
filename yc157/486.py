S = input()

e = S.find('OOO')
w = S.find('XXX')

if e == -1 and w == -1:
    print('NA')
elif e == -1:
    print('West')
elif w == -1:
    print('East')
elif e < w:
    print('East')
elif e > w:
    print('West')
