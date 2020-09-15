n = input()

t = int(n.replace('hamu', '1').replace('ham', '0'), 2)
t *= 2
print(bin(t)[2:].replace('1', 'hamu').replace('0', 'ham'))
