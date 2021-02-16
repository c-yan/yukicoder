package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var (
	x uint32 = 0
	y uint32 = 1
	z uint32 = 2
	w uint32 = 3
)

func xorshift() uint32 {
	var t uint32 = x ^ (x << 11)
	x = y
	y = z
	z = w
	w = (w ^ (w >> 19)) ^ (t ^ (t >> 8))
	return w
}

const (
	totalSize = 10000001
	buffSize  = 10000
)

func main() {
	defer flush()

	x = uint32(readInt())

	t := make([]int, 0, totalSize/10+1)
	buff := make([]int, buffSize)
	for i := 0; i < totalSize/buffSize; i++ {
		for j := 0; j < buffSize; j++ {
			buff[j] = int(xorshift())
		}
		sort.Ints(buff)
		a := (buffSize - (buffSize / 10)) / 2
		t = append(t, buff[a:a+buffSize/10]...)
	}
	t = append(t, int(xorshift()))
	sort.Ints(t)
	println(t[len(t)/2])
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
