package algo

import "fmt"

// 처음 방법 22 ms Beats 24.13%
func twoSum_lagacy(nums []int, target int) []int {
	// 2 for
	result := make([]int, 0, 2)
	for i, v := range nums {
		result = append(result, i)
		for j := i + 1; j < len(nums); j++ {
			if target-v-nums[j] == 0 {
				fmt.Println(v, nums[j])
				result = append(result, j)
				return result
			}
		}
		result = result[:0]
	}
	return []int{}
}
func twoSum(nums []int, target int) []int {
	table := make(map[int]int)
	for i, v := range nums {
		if idx, ok := table[target-v]; ok {
			return []int{idx, i}
		}
		table[v] = i
	}
	return nil

}
