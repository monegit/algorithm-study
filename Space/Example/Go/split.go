package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "hello world"
	for i := 0; i < len(strings.Split(str, " ")); i++ {
		fmt.Printf("split array %dth element: %s\n",
			i,
			strings.Split(str, " ")[i])
	}
}
