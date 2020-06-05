package main

func main() {
	arr := []int{1, 2, 3, 4}

	print(sum(arr))
}

func sum(a []int) int {
	result := 0
	for i := 0; i < len(a); i++ {
		result += a[i]
	}
	return result
}
