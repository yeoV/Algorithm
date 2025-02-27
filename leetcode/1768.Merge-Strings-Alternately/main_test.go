package algo

import (
	"fmt"
	"testing"
)

type param struct {
	word1 string
	word2 string
}

func TestMergeAlternately(t *testing.T) {
	params := []param{
		{"ab", "abbcde"},
		{"12345", "12"},
	}
	fmt.Println("========== 1768. Problem ============")

	for _, param := range params {
		fmt.Printf("【input】:%s,%s   【output】:%s\n", param.word1, param.word2, mergeAlternately(param.word1, param.word2))
	}
}
