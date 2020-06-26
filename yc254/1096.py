from itertools import accumulate


class SegmentTree():
    _data = []
    _offset = 0
    _size = 0

    def __init__(self, size):
        _size = size
        t = 1
        while t < size:
            t *= 2
        self._offset = t - 1
        self._data = [0 for _ in range(t * 2 - 1)]

    def update_all(self, iterable):
        data = self._data
        data[self._offset:self._offset + self._size] = iterable
        for i in range(self._offset - 1, -1, -1):
            data[i] = data[i * 2 + 1] + data[i * 2 + 2]

    def query(self, start, stop):
        result = 0
        l = start + self._offset
        r = stop + self._offset
        while l < r:
            if l & 1 == 0:
                result = result + self._data[l]
            if r & 1 == 0:
                result = result + self._data[r - 1]
            l = l // 2
            r = (r - 1) // 2
        return result


N, *A = map(int, open(0).read().split())

a = list(accumulate(A))

st = SegmentTree(N)
st.update_all(a)

#print(a)
result = 0
result += st.query(0, N)
#print(result)
for i in range(1, N):
    result += st.query(i, N) - a[i - 1] * (N - i)
    #print(result)
print(result)
