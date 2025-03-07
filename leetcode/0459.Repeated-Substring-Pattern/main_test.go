package leetcode

import (
	"fmt"
	"testing"
)

type param struct {
	s string
}

func TestRepeatedSubstringPattern(t *testing.T) {
	q := []param{
		{"abababa"},
		{"abcabcabc"},
		{"abab"},
	}

	fmt.Println("=====================problem 0459==========================")
	for _, val := range q {
		fmt.Printf("【input】:%v   【output】:%v\n", val.s, repeatedSubstringPattern(val.s))
	}
}
