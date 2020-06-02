package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}

	fmt.Printf(
		`len: %d
		array: %v`,
		len(a), a)
}
