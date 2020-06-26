S = list(map(int, input().split()))

S.sort()
print('%.2f' % (sum(S[1:5]) / 4))
