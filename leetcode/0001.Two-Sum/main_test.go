package algo

import (
	"fmt"
	"testing"
)

type question struct {
	param
	ans
}

type ans struct {
	result []int
}
type param struct {
	nums   []int
	target int
}

func TestTwoSum(t *testing.T) {
	q := []question{
		{param{[]int{3, 2, 4}, 6},
			ans{[]int{1, 2}}},

		{param{[]int{2, 7, 11, 15}, 9},
			ans{[]int{0, 1}}},

		{param{[]int{2, 7, 11, 15}, 16},
			ans{[]int{}}},
	}

	fmt.Println("=====================problem 0001==========================")

	for _, qs := range q {
		p, _ := qs.param, qs.ans
		fmt.Printf("【input】:%v       【output】:%v\n", p, twoSum(p.nums, p.target))
	}
}
