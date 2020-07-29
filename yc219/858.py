A, B = map(int, input().split())

result = "%d." % (A // B)
t = A % B
for i in range(50):
    result += "%d" % (t * 10 // B)
    t = t * 10 % B
print(result)
