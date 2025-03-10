package leetcode

import (
	"testing"
)

type param struct {
	nums []int
}

func TestMoveZeroes(t *testing.T) {

	params := []param{
		{[]int{0, 1, 0, 3, 12}},
	}

	for _, p := range params {
		moveZeroes(p.nums)

	}

}
