package leetcode

import (
	"fmt"
	"testing"
)

type param struct {
	s string
	t string
}

func TestIsAnagram(t *testing.T) {
	params := []param{
		{"a", "abb"},
	}
	fmt.Println("========== 0242. Problem ============")

	for _, p := range params {
		fmt.Printf("【input】:%s,%s   【output】:%v\n", p.s, p.t, isAnagram(p.s, p.t))
	}
}
