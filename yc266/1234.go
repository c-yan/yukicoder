package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

const (
	defaultValue = math.MaxInt64
	defaultLazy  = 0
)

type segmentTree struct {
	offset int
	values []int
	lazy   []int
}

func newSegmentTree(n int) segmentTree {
	var result segmentTree
	t := 1
	for t < n {
		t *= 2
	}
	result.offset = t - 1
	result.values = make([]int, 2*t-1)
	result.lazy = make([]int, 2*t-1)
	for i := 0; i < 2*t-1; i++ {
		result.values[i] = defaultValue
		result.lazy[i] = defaultLazy
	}
	return result
}

func op(x, y int) int {
	return min(x, y)
}

func (st segmentTree) build(a []int) {
	for i, v := range a {
		st.values[st.offset+i] = v
	}
	for i := st.offset - 1; i > -1; i-- {
		st.values[i] = op(st.values[i*2+1], st.values[i*2+2])
	}
}

func (st segmentTree) segments(start, stop int) []int {
	result := make([]int, 0, 20)
	l := start + st.offset
	r := stop + st.offset
	for l < r {
		if l&1 == 0 {
			result = append(result, l)
		}
		if r&1 == 0 {
			result = append(result, r-1)
		}
		l = l / 2
		r = (r - 1) / 2
	}
	return result
}

func (st segmentTree) propagate(segments []int) {
	for _, i := range segments {
		indexes := make([]int, 0, 20)
		for i != 0 {
			i = (i - 1) / 2
			indexes = append(indexes, i)
		}
		for len(indexes) != 0 {
			j := indexes[len(indexes)-1]
			indexes = indexes[:len(indexes)-1]
			if st.lazy[j] == defaultLazy {
				continue
			}
			st.lazy[j*2+1] += st.lazy[j]
			st.values[j*2+1] += st.lazy[j]
			st.lazy[j*2+2] += st.lazy[j]
			st.values[j*2+2] += st.lazy[j]
			st.lazy[j] = defaultLazy
		}
	}
}

func (st segmentTree) apply(start, stop int, value int) {
	segments := st.segments(start, stop)
	st.propagate(segments)
	for _, i := range segments {
		st.lazy[i] += value
		st.values[i] += value
		for i != 0 {
			i = (i - 1) / 2
			st.values[i] = op(st.values[i*2+1], st.values[i*2+2])
		}
	}
}

func (st segmentTree) query(start, stop int) int {
	segments := st.segments(start, stop)
	st.propagate(segments)
	result := defaultValue
	for _, i := range segments {
		result = op(result, st.values[i])
	}
	return result
}

func main() {
	defer flush()

	N := readInt()
	a := make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}
	Q := readInt()

	st := newSegmentTree(N)
	st.build(a)
	for i := 0; i < Q; i++ {
		k := readInt()
		l := readInt()
		r := readInt()
		c := readInt()
		if k == 1 {
			st.apply(l-1, r, c)
		} else if k == 2 {
			println(st.query(l-1, r))
		}
	}
}

const (
	ioBufferSize = 1 * 1024 * 1024 // 1 MB
)

var stdinScanner = func() *bufio.Scanner {
	result := bufio.NewScanner(os.Stdin)
	result.Buffer(make([]byte, ioBufferSize), ioBufferSize)
	result.Split(bufio.ScanWords)
	return result
}()

func readString() string {
	stdinScanner.Scan()
	return stdinScanner.Text()
}

func readInt() int {
	result, err := strconv.Atoi(readString())
	if err != nil {
		panic(err)
	}
	return result
}

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
