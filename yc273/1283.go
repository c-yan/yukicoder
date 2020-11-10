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

func main() {
	defer flush()

	N := readInt()
	M := readInt()

	c := make([][]int, N)
	for i := 0; i < N; i++ {
		c[i] = make([]int, N)
	}

	for i := 0; i < M; i++ {
		h := readInt() - 1
		w := readInt() - 1
		c[h][w] = readInt()
	}

	dpa := make([][]int, N)
	dpb := make([][]int, N)
	for i := 0; i < N; i++ {
		dpa[i] = make([]int, N)
		dpb[i] = make([]int, N)
		for j := 0; j < N; j++ {
			dpa[i][j] = math.MaxInt64 >> 1
			dpb[i][j] = math.MaxInt64 >> 1
		}
	}
	dpa[0][0] = 0

	q := make([][3]int, 0)
	q = append(q, [3]int{0, 0, 0})
	for len(q) != 0 {
		y := q[0][0]
		x := q[0][1]
		t := q[0][2]
		q = q[1:]

		if t == 0 {
			if y != 0 {
				if dpa[y-1][x] > dpa[y][x]+1+c[y-1][x] {
					dpa[y-1][x] = dpa[y][x] + 1 + c[y-1][x]
					q = append(q, [3]int{y - 1, x, 0})
				}
				if c[y-1][x] > 0 {
					if dpb[y-1][x] > dpa[y][x]+1 {
						dpb[y-1][x] = dpa[y][x] + 1
						q = append(q, [3]int{y - 1, x, 1})
					}
				}
			}
			if y != N-1 {
				if dpa[y+1][x] > dpa[y][x]+1+c[y+1][x] {
					dpa[y+1][x] = dpa[y][x] + 1 + c[y+1][x]
					q = append(q, [3]int{y + 1, x, 0})
				}
				if c[y+1][x] > 0 {
					if dpb[y+1][x] > dpa[y][x]+1 {
						dpb[y+1][x] = dpa[y][x] + 1
						q = append(q, [3]int{y + 1, x, 1})
					}
				}
			}
			if x != 0 {
				if dpa[y][x-1] > dpa[y][x]+1+c[y][x-1] {
					dpa[y][x-1] = dpa[y][x] + 1 + c[y][x-1]
					q = append(q, [3]int{y, x - 1, 0})
				}
				if c[y][x-1] > 0 {
					if dpb[y][x-1] > dpa[y][x]+1 {
						dpb[y][x-1] = dpa[y][x] + 1
						q = append(q, [3]int{y, x - 1, 1})
					}
				}
			}
			if x != N-1 {
				if dpa[y][x+1] > dpa[y][x]+1+c[y][x+1] {
					dpa[y][x+1] = dpa[y][x] + 1 + c[y][x+1]
					q = append(q, [3]int{y, x + 1, 0})
				}
				if c[y][x+1] > 0 {
					if dpb[y][x+1] > dpa[y][x]+1 {
						dpb[y][x+1] = dpa[y][x] + 1
						q = append(q, [3]int{y, x + 1, 1})
					}
				}
			}
		} else {
			if y != 0 {
				if dpb[y-1][x] > dpb[y][x]+1+c[y-1][x] {
					dpb[y-1][x] = dpb[y][x] + 1 + c[y-1][x]
					q = append(q, [3]int{y - 1, x, 1})
				}
			}
			if y != N-1 {
				if dpb[y+1][x] > dpb[y][x]+1+c[y+1][x] {
					dpb[y+1][x] = dpb[y][x] + 1 + c[y+1][x]
					q = append(q, [3]int{y + 1, x, 1})
				}
			}
			if x != 0 {
				if dpb[y][x-1] > dpb[y][x]+1+c[y][x-1] {
					dpb[y][x-1] = dpb[y][x] + 1 + c[y][x-1]
					q = append(q, [3]int{y, x - 1, 1})
				}
			}
			if x != N-1 {
				if dpb[y][x+1] > dpb[y][x]+1+c[y][x+1] {
					dpb[y][x+1] = dpb[y][x] + 1 + c[y][x+1]
					q = append(q, [3]int{y, x + 1, 1})
				}
			}
		}
	}
	println(min(dpa[N-1][N-1], dpb[N-1][N-1]))
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
