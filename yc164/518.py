def r2i(s):
    i = 0
    result = 0
    while i < len(s):
        a = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        if s[i:i + 2] in a:
            result += a[s[i:i + 2]]
            i += 2
            continue
        b = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result += b[s[i]]
        i += 1
    return result


def i2r(i):
    if i > 3999:
        return 'ERROR'
    result = ''
    while i != 0:
        if i >= 1000:
            result += 'M'
            i -= 1000
        elif i >= 900:
            result += 'CM'
            i -= 900
        elif i >= 500:
            result += 'D'
            i -= 500
        elif i >= 400:
            result += 'CD'
            i -= 400
        elif i >= 100:
            result += 'C'
            i -= 100
        elif i >= 90:
            result += 'XC'
            i -= 90
        elif i >= 50:
            result += 'L'
            i -= 50
        elif i >= 40:
            result += 'XL'
            i -= 40
        elif i >= 10:
            result += 'X'
            i -= 10
        elif i >= 9:
            result += 'IX'
            i -= 9
        elif i >= 5:
            result += 'V'
            i -= 5
        elif i >= 4:
            result += 'IV'
            i -= 4
        elif i >= 1:
            result += 'I'
            i -= 1
    return result


N = int(input())
R = input().split()

print(i2r(sum(r2i(r) for r in R)))
