def is_ok(s):
    if len(s) > 1 and s[0] == '0':
        return False
    for c in s:
        if c not in '0123456789':
            return False
    if int(s) > 12345:
        return False
    return True


A = input()
B = input()

if is_ok(A) and is_ok(B):
    print('OK')
else:
    print('NG')
