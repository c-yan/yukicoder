S = input()

if all(s == 'AC' for s in S.split(',')):
    print('Done!')
else:
    print('Failed...')
