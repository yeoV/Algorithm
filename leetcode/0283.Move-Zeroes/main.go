package leetcode

func moveZeroes(nums []int) {
	var left int16

	for i := range nums {
		if nums[i] != 0 {
			nums[left] = nums[i]
			left++
		}
	}

	// fill zeros
	for ; left < int16(len(nums)); left++ {
		nums[left] = 0
	}
}
