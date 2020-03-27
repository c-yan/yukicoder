T = input()

hh, mm = map(int, T.split(':'))

mm += 5
if mm > 59:
    hh += 1
    mm %= 60
if hh > 23:
    hh %= 24

print('%02d:%02d' % (hh, mm))
