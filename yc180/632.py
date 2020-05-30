c = input()

def is_kadomatsu(c):
    return c[1] > max(c[0], c[2]) or c[1] < min(c[0], c[2])

result = []
if is_kadomatsu(list(map(int, c.replace('?', '1').split()))):
    result.append('1')
if is_kadomatsu(list(map(int, c.replace('?', '4').split()))):
    result.append('4')
print(''.join(result))
