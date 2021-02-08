from sys import stdin


class SegmentTree:
    DEFAULT_VALUE = 10 ** 18
    DEFAULT_LAZY = 0
    op = min

    def __init__(self, size):
        self._size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._values = [SegmentTree.DEFAULT_VALUE] * (t * 2 - 1)
        self._lazy = [SegmentTree.DEFAULT_LAZY] * (t * 2 - 1)

    def build(self, iterable):
        op = SegmentTree.op
        values = self._values
        values[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            values[i] = SegmentTree.op(values[i * 2 + 1], values[i * 2 + 2])

    def _get_segmen_indexes(self, start, stop):
        ls = []
        rs = []
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                ls.append(l)
            if r & 1 == 0:
                rs.append(r - 1)
            l = l // 2
            r = (r - 1) // 2
        return ls + rs[::-1]

    def _propagate(self, start, stop):
        lazy = self._lazy
        values = self._values
        indexes = []
        for i in self._get_segmen_indexes(start, stop):
            if i == 0:
                return
            while i != 0:
                i = (i - 1) // 2
                indexes.append(i)
        for i in sorted(set(indexes)):
            l = lazy[i]
            if l == SegmentTree.DEFAULT_LAZY:
                continue
            lazy[i * 2 + 1] += l
            values[i * 2 + 1] += l
            lazy[i * 2 + 2] += l
            values[i * 2 + 2] += l
            lazy[i] = SegmentTree.DEFAULT_LAZY

    def apply(self, start, stop, value):
        op = SegmentTree.op
        values = self._values
        lazy = self._lazy
        self._propagate(start, stop)
        for i in self._get_segmen_indexes(start, stop):
            lazy[i] += value
            values[i] += value
            while i >= 1:
                i = (i - 1) // 2
                values[i] = op(values[i * 2 + 1], values[i * 2 + 2])

    def query(self, start, stop):
        op = SegmentTree.op
        values = self._values
        self._propagate(start, stop)
        result = SegmentTree.DEFAULT_VALUE
        for i in self._get_segmen_indexes(start, stop):
            result = op(result, values[i])
        return result


readline = stdin.readline

N = int(readline())
a = list(map(int, readline().split()))
Q = int(readline())

st = SegmentTree(N)
st.build(a)
result = []
for _ in range(Q):
    k, l, r, c = map(int, readline().split())
    if k == 1:
        st.apply(l - 1, r, c)
    elif k == 2:
        result.append(st.query(l - 1, r))
print(*result, sep='\n')
