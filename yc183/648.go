package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	n := readInt()

	ok := 0
	ng := 2000000000
	for ng-ok > 1 {
		m := ok + (ng-ok)/2
		if m*(m+1)/2 <= n {
			ok = m
		} else {
			ng = m
		}
	}

	if ok*(ok+1)/2 == n {
		println("YES")
		println(ok)
	} else {
		println("NO")
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
