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

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	defer flush()

	N := readInt()
	Y := make([]int, N)
	for i := 0; i < N; i++ {
		Y[i] = readInt()
	}

	dp := make([][]int, N)
	for i := 0; i < N; i++ {
		dp[i] = make([]int, 10000+1)
	}

	for j := 0; j < 10000+1; j++ {
		dp[0][j] = abs(Y[0] - j)
	}

	for i := 1; i < N; i++ {
		t := math.MaxInt64
		for j := 0; j < 10000+1; j++ {
			t = min(t, dp[i-1][j])
			dp[i][j] = t + abs(Y[i]-j)
		}
	}

	result := math.MaxInt64
	for j := 0; j < 10000+1; j++ {
		result = min(result, dp[N-1][j])
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

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
