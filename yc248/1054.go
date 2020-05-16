package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func find(parent []int, amount []int, i int) (int, int) {
	if parent[i] < 0 {
		return i, 0
	}
	j, a := find(parent, amount, parent[i])
	parent[i] = j
	amount[i] += a
	return parent[i], amount[i]
}

func unite(parent []int, amount []int, i, j int) {
	i, _ = find(parent, amount, i)
	j, _ = find(parent, amount, j)
	if i == j {
		return
	}
	parent[j] += parent[i]
	parent[i] = j
	amount[i] -= amount[j]
}

func main() {
	defer flush()

	N := readInt()
	Q := readInt()

	parent := make([]int, N+1)
	amount := make([]int, N+1)
	for i := 0; i < N+1; i++ {
		parent[i] = -1
	}
	for i := 0; i < Q; i++ {
		T := readInt()
		A := readInt()
		B := readInt()

		if T == 1 {
			unite(parent, amount, A, B)
		} else if T == 2 {
			j, _ := find(parent, amount, A)
			amount[j] += B
		} else if T == 3 {
			j, a := find(parent, amount, A)
			println(amount[j] + a)
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

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
