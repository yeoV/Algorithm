package leetcode

import (
	"fmt"
	"testing"
)

type params struct {
	s string
	t string
}

func TestFindTheDifference(t *testing.T) {
	q := []params{
		{"abc", "abcd"},
		{"a", "aa"},
	}

	fmt.Println("=====================problem 0389==========================")

	for _, val := range q {
		fmt.Printf("【input】:%v       【output】:%v\n", val, findTheDifference(val.s, val.t))

	}

}
