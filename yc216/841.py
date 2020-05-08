S1, S2 = input().split()

if S1 in ['Sat', 'Sun']:
    if S2 in ['Sat', 'Sun']:
        print('8/33')
    else:
        print('8/32')
else:
    print('8/31')
