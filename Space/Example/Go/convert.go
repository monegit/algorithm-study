package main

import (
	"strconv"
)

func main() {
	// ex1 String To Int
	str1, _ := strconv.Atoi("100")
	println(str1 + 1)

	// ex2 Int To String
	str2 := strconv.Itoa(100)
	println(str2)

	// ex3 String To Int
	if str3, err := strconv.Atoi("100l"); err == nil {
		println(str3)
	} else {
		println(err)
	}
}
