package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	var sqrt int = 1
	var count int = 1

	input := bufio.NewScanner(os.Stdin)
	if input.Scan() {
		for {
			i, _ := strconv.Atoi(input.Text())
			if sqrt >= i {
				break
			}

			sqrt += 6 * count
			count++
		}
	}

	print(count)
}
