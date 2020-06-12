package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// #1
	scanner := bufio.NewScanner(os.Stdin)
	if scanner.Scan() {
		println(scanner.Text())
	}

	// #2
	var i int
	fmt.Scanf("%d", &i)

	fmt.Printf("%d", i)
}
