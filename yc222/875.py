from sys import stdin


class SegmentTree:
    def __init__(self, size, op, e):
        self._op = op
        self._e = e
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [e] * (t * 2 - 1)

    def __getitem__(self, key):
        return self._data[self._offset + key]

    def __setitem__(self, key, value):
        op = self._op
        data = self._data
        i = self._offset + key
        data[i] = value
        while i >= 1:
            i = (i - 1) // 2
            data[i] = op(data[i * 2 + 1], data[i * 2 + 2])

    def build(self, iterable):
        op = self._op
        data = self._data
        data[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            data[i] = op(data[i * 2 + 1], data[i * 2 + 2])

    def query(self, start, stop):
        def iter_segments(data, l, r):
            while l < r:
                if l & 1 == 0:
                    yield data[l]
                if r & 1 == 0:
                    yield data[r - 1]
                l = l // 2
                r = (r - 1) // 2
        op = self._op
        it = iter_segments(self._data, start + self._offset,
                           stop + self._offset)
        result = self._e
        for v in it:
            result = op(result, v)
        return result


def f(a, b):
    if a[1] < b[1]:
        return a
    else:
        return b


readline = stdin.readline

N, Q = map(int, readline().split())
a = list(map(int, input().split()))

st = SegmentTree(N, f, (N + 1, N + 1))
st.build((i + 1, a[i]) for i in range(N))

result = []
for _ in range(Q):
    t, l, r = map(int, readline().split())
    l, r = l - 1, r - 1
    if t == 1:
        lv = st[l][1]
        rv = st[r][1]
        st[l] = (l + 1, rv)
        st[r] = (r + 1, lv)
    elif t == 2:
        result.append(st.query(l, r + 1)[0])
print(*result, sep='\n')
