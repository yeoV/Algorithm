package leetcode

import (
	"fmt"
	"testing"
)

type params struct {
	haystack string
	needle   string
}

func TestStrStr(t *testing.T) {
	params := []params{
		{"sadbutsad", "sad"},
		{"leetcode", "leeto"},
	}

	fmt.Println("========== 0028. Problem ============")

	for _, p := range params {
		fmt.Printf("【input】:%s,%s   【output】:%d\n", p.haystack, p.needle, strStr(p.haystack, p.needle))
	}
}
