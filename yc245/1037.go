package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	defer flush()

	N := readInt()
	V := readInt()
	L := readInt()

	cx := 0
	d := map[int]int{}
	d[V] = 0
	for i := 0; i < N; i++ {
		x := readInt()
		v := readInt()
		w := readInt()
		nd := map[int]int{}

		for k := range d {
			t := k - (x - cx)
			if t < 0 {
				continue
			}
			_, ok := nd[t]
			if !ok || nd[t] > d[k] {
				nd[t] = d[k]
			}
			t = min(t+v, V)
			_, ok = nd[t]
			if !ok || nd[t] > d[k]+w {
				nd[t] = d[k] + w
			}
		}

		if len(nd) == 0 {
			println(-1)
			return
		}
		d = nd
		cx = x
	}

	result := math.MaxInt64
	for k := range d {
		if k-(L-cx) >= 0 {
			result = min(result, d[k])
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

func readInts(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = readInt()
	}
	return result
}

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
