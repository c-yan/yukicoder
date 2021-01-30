def is_kadomatsu(a, b, c):
    if a == b or b == c or a == c:
        return False
    return min([a, b, c]) == b or max([a, b, c]) == b


a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

if is_kadomatsu(b1, a2, a3) and is_kadomatsu(a1, b2, b3):
    print('Yes')
elif is_kadomatsu(b2, a2, a3) and is_kadomatsu(b1, a1, b3):
    print('Yes')
elif is_kadomatsu(b3, a2, a3) and is_kadomatsu(b1, b2, a1):
    print('Yes')
elif is_kadomatsu(a1, b1, a3) and is_kadomatsu(a2, b2, b3):
    print('Yes')
elif is_kadomatsu(a1, b2, a3) and is_kadomatsu(b1, a2, b3):
    print('Yes')
elif is_kadomatsu(a1, b3, a3) and is_kadomatsu(b1, b2, a2):
    print('Yes')
elif is_kadomatsu(a1, a2, b1) and is_kadomatsu(a3, b2, b3):
    print('Yes')
elif is_kadomatsu(a1, a2, b2) and is_kadomatsu(b1, a3, b3):
    print('Yes')
elif is_kadomatsu(a1, a3, b3) and is_kadomatsu(b1, b2, a3):
    print('Yes')
else:
    print('No')
