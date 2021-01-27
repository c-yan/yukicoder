D = '0.1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495969798991'

N = int(input())

a = [0] * len(D)
for i in range(2, len(D)):
    a[i] = int(D[i])

result = [0] * len(D)

x = N % 10
for i in range(len(D) - 1, 0, -1):
    t = a[i] * x
    result[i] += t

x = (N // 10) % 10
for i in range(len(D) - 1, 0, -1):
    t = a[i] * x
    result[i - 1] += t

x = (N // 100) % 10
for i in range(len(D) - 1, 0, -1):
    t = a[i] * x
    result[i - 2] += t

for i in range(len(D) - 1, 0, -1):
    if result[i] >= 10:
        result[i - 1] += result[i] // 10
        result[i] %= 10

s = ''.join(str(x) for x in result)
s = s[:2] + '.' + s[2:]
if s[0] == '0':
    s = s[1:]
print(s.rstrip('0'))
