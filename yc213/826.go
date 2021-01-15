package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func find(parent []int, i int) int {
	if parent[i] < 0 {
		return i
	}
	parent[i] = find(parent, parent[i])
	return parent[i]
}

func unite(parent []int, i, j int) {
	i = find(parent, i)
	j = find(parent, j)
	if i == j {
		return
	}
	parent[j] += parent[i]
	parent[i] = j
}

func isqrt(n int) int {
	if n < 0 {
		panic("isqrt argument must be nonnegative")
	}

	if n <= 1 {
		return n
	}

	ok := 0
	ng := 3037000500 // 3037000499 * 3037000499 < math.MaxInt64 < 3037000500 * 3037000500
	if n < ng {
		ng = n
	}
	for ng-ok > 1 {
		m := ok + (ng-ok)/2
		if m*m <= n {
			ok = m
		} else {
			ng = m
		}
	}
	return ok
}

func makePrimeTable(n int) []int {
	sieve := make([]int, n+1)
	for i := 0; i < n+1; i++ {
		sieve[i] = i
	}
	sieve[0] = -1
	sieve[1] = -1
	for i := 4; i < n+1; i += 2 {
		sieve[i] = 2
	}
	for i := 3; i < isqrt(n)+1; i += 2 {
		if sieve[i] != i {
			continue
		}
		for j := i * i; j < n+1; j += i * 2 {
			if sieve[j] == j {
				sieve[j] = i
			}
		}
	}
	return sieve
}

func main() {
	defer flush()

	N := readInt()
	P := readInt()

	parent := make([]int, N+1)
	for i := 0; i < N+1; i++ {
		parent[i] = -1
	}

	sieve := makePrimeTable(N)
	for j := 2 * 2; j < N+1; j += 2 {
		unite(parent, 2, j)
	}
	for i := 3; i < N+1; i++ {
		if sieve[i] != i {
			continue
		}
		if 2*i <= N {
			unite(parent, 2, i)
		}
		for j := i * i; j < N+1; j += i * 2 {
			unite(parent, i, j)
		}
	}
	println(-parent[find(parent, P)])
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
