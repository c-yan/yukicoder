from operator import add
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

    def __iter__(self):
        for i in range(self._size):
            yield self[i]

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


def shrink(a):
    inv = sorted(set(a))
    n = len(inv)
    fwd = {}
    for i in range(n):
        fwd[inv[i]] = i
    return n, fwd, inv


readline = stdin.readline

Q, K = map(int, readline().split())
query = [readline() for _ in range(Q)]

a = []
for q in query:
    if q[0] != '1':
        continue
    a.append(int(q[2:]))
n, fwd, inv = shrink(a)

st = SegmentTree(n, add, 0)
k = 0
result = []
for q in query:
    if q[0] == '1':
        v = fwd[int(q[2:])]
        st[v] += 1
        k += 1
    elif q[0] == '2':
        if k < K:
            result.append(-1)
            continue
        ok = n
        ng = -1
        while ok - ng > 1:
            m = ng + (ok - ng) // 2
            if st.query(0, m) >= K:
                ok = m
            else:
                ng = m
        result.append(inv[ok - 1])
        st[ok - 1] -= 1
        k -= 1
print(*result, sep='\n')
