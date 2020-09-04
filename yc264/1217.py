S = input()

for i in range(26):
    a = chr(i + ord('a'))
    if S[i] == a:
        continue
    print('%sto%s' % (a, S[i]))
    break
