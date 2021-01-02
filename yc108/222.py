def read_int(s, i):
    j = i
    if s[i] in '+-':
        j += 1
    while j < len(s) and s[j] in '0123456789':
        j += 1
    return int(s[i:j]), j


xopy = input()
x, i = read_int(xopy, 0)
op = xopy[i]
y, _ = read_int(xopy, i + 1)

if op == '+':
    print(x - y)
elif op == '-':
    print(x + y)
