package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	_input := bufio.NewScanner(os.Stdin)
	var sb strings.Builder

	if _input.Scan() {
		convi, _ := strconv.Atoi(_input.Text())
		exp := int(math.Ceil(float64(convi) / 2))

		for u := 0; u < exp; u++ {
			fmt.Fprintf(&sb, " %c", '*')
		}
		fmt.Fprintln(&sb)
		for d := 0; d < convi-exp; d++ {
			fmt.Fprintf(&sb, " %c", '*')
		}

		for i := 0; i < convi; i++ {
			fmt.Println(strings.Trim(sb.String(), " "))
		}
	}
}
