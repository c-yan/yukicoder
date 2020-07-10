package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	m = 1000000007
)

func main() {
	defer flush()

	N := readInt()
	M := readInt()
	K := readInt()

	pqc := make([][][2]int, 301)
	for i := 0; i < M; i++ {
		P := readInt()
		Q := readInt()
		C := readInt()
		pqc[P] = append(pqc[P], [2]int{Q, C})
	}

	t := make([]map[int]int, 301)
	for i := 1; i < 301; i++ {
		t[i] = map[int]int{0: 1}
	}
	for i := 0; i < N-1; i++ {
		nt := make([]map[int]int, 301)
		for j := 1; j < 301; j++ {
			for k := range t[j] {
				for _, qc := range pqc[j] {
					q := qc[0]
					c := qc[1]
					v := k + c
					if nt[q] == nil {
						nt[q] = map[int]int{}
					}
					if v <= K {
						nt[q][v] += t[j][k]
						nt[q][v] %= m
					}
				}
			}
		}
		t = nt
	}

	result := 0
	for i := 1; i < 301; i++ {
		result += t[i][K]
		result %= m
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
