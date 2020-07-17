package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	char := []byte{0xef, 0xbf, 0xbd, 0}
	r, _ := utf8.DecodeRune(char)
	fmt.Printf("%c", r)
}
