package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func appendSorted(a []int, b int) []int {
	i := sort.Search(len(a), func(i int) bool { return a[i] >= b })
	a = append(a, 0)
	copy(a[i+1:], a[i:])
	a[i] = b
	return a
}

func main() {
	defer flush()

	N := readInt()
	a := make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}
	b := make([]int, N)
	for i := 0; i < N; i++ {
		b[i] = readInt()
	}
	sort.Ints(a)

	t0 := make([]int, 0, N)
	t1 := make([]int, 0, 5000)
	result := 0
	for i := 0; i < N; i++ {
		result += sort.Search(len(t0), func(j int) bool { return t0[j] >= a[i] })
		t1 = appendSorted(t1, b[i])
		result += sort.Search(len(t1), func(j int) bool { return t1[j] >= a[i] })
		if len(t1) == 5000 {
			t0 = append(t0, t1...)
			sort.Ints(t0)
			t1 = t1[:0]
		}
	}
	println(result)
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
