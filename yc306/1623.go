package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// BIT stands for binary indexed tree.
type BIT []int

func newBIT(n int) BIT {
	return make([]int, n)
}

func (bit BIT) add(i, v int) {
	for i++; i <= len(bit); i += i & -i {
		bit[i-1] += v
	}
}

func (bit BIT) sum(i int) int {
	result := 0
	for i++; i > 0; i -= i & -i {
		result += bit[i-1]
	}
	return result
}

func (bit BIT) query(start int, stop int) int {
	return bit.sum(stop-1) - bit.sum(start-1)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	defer flush()

	n := readInt()
	r := make([]int, n)
	for i := 0; i < n; i++ {
		r[i] = readInt()
	}
	g := make([]int, n)
	for i := 0; i < n; i++ {
		g[i] = readInt()
	}
	b := make([]int, n)
	for i := 0; i < n; i++ {
		b[i] = readInt()
	}

	rr := make([]int, 3001)
	for i := 0; i < n; i++ {
		rr[r[i]]++
	}
	gg := make([]int, 3001)
	for i := 0; i < n; i++ {
		gg[g[i]]++
	}
	bb := make([]int, 3001)
	for i := 0; i < n; i++ {
		bb[b[i]]++
	}

	gb := make([][]int, 3001)
	for i := 0; i < 3001; i++ {
		if gg[i] == 0 {
			continue
		}
		for j := 0; j < 3001; j++ {
			if bb[j] == 0 {
				continue
			}
			gb[max(i, j)] = append(gb[max(i, j)], i<<12+j)
		}
	}

	result := 0
	bit := newBIT(6001)
	for i := 0; i < 3001; i++ {
		for _, v := range gb[i] {
			x := v >> 12
			y := v & 4095
			bit.add(x+y, gg[x]*bb[y])
		}
		result += rr[i] * bit.query(i+1, 6001)
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
