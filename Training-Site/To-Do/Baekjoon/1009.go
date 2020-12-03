package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var input1 int
	var input2 string

	fmt.Scan(&input1)
	fmt.Println(input1)

	for i := 0; i < input1; i++ {
		input := bufio.NewScanner(os.Stdin)

		if input.Scan() {
			input2 := input.Text
		}
		fmt.Println("dd", input2)
		tmp1, _ := strconv.ParseFloat(strings.Split(input2, " ")[0], 64)
		fmt.Println(tmp1)
		//tmp2, _ := strconv.ParseFloat(strings.Split(input2, " ")[1], 64)
		//fmt.Println(tmp2)

		//fmt.Println(math.Pow(tmp1, tmp2))
	}
}
