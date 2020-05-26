a = int(input())

t = a * 60 // 100
print('%02d:%02d' % (10 + t // 60, t % 60))
