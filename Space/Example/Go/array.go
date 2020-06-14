package main

import "fmt"

func main() {
	arr := []int{1, 2, 3, 4, 5}
	arr = append(arr, 10)
	_arr := &arr

	fmt.Printf("len: %d\n"+
		"array: %v\n"+
		"_array[0]: %d\n",
		len(arr), arr, (*_arr)[0])
}
