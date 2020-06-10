S1 = input()
S2 = input()
S3 = input()

t = {'RED': 0, 'BLUE': 0}

t[S1] += 1
t[S2] += 1
t[S3] += 1

if t['RED'] > t['BLUE']:
    print('RED')
else:
    print('BLUE')
