Y, M, D = map(int, input().split())

s = '%04d%02d%02d' % (Y, M, D)
if '19890108' <= s <= '20190430':
    print('Yes')
else:
    print('No')
