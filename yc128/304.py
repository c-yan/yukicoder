from sys import stdin, stdout

for i in range(1000):
    stdout.write('%03d\n' % i)
    stdout.flush()
    result = stdin.readline().rstrip()
    if result == 'unlocked':
        break
