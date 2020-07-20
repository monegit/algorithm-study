package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewScanner(os.Stdin)
	if reader.Scan() {
		arr := strings.Split(reader.Text(), " ")
		fmt.Println(StringToInt(arr[0]) * StringToInt(arr[1]))
	}
}

func StringToInt(str string) int {
	result, _ := strconv.Atoi(str)
	return result
}