S = input()

result = S[0]
for c in S[1:]:
    if c == result[-1]:
        continue
    result += c
print(result)
