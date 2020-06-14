package main

import "fmt"

func main() {
	arr := []int{2, 3, 4, 1, 4, 5}

	fmt.Printf("%v\n", StartToEndBubbleSort(arr))
}

func StartToEndBubbleSort(array []int) []int {
	arr := array
	temp := 0

	for ii := 0; ii < 4; ii++ {
		for i := 0; i < len(arr)-1; i++ {
			if arr[i] > arr[i+1] {
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
			}
		}
	}

	return arr
}
