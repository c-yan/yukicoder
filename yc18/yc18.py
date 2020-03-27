S = input()

result = []
for i in range(len(S)):
    result.append(chr((ord(S[i]) - ord('A') - (i + 1)) % 26 + ord('A')))
print(''.join(result))
