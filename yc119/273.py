def is_palindrome(s):
    return s == s[::-1]


S = input()

result = 0
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        if i == 0 and j == len(S):
            continue
        if not is_palindrome(S[i:j]):
            continue
        result = max(result, j - i)
print(result)
