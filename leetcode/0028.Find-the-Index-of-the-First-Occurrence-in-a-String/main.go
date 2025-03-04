package leetcode

func strStr(haystack string, needle string) int {
	n, m := len(haystack), len(needle)

	for i := range n - m + 1 {
		if haystack[i:i+m] == string(needle) {
			return i
		}
	}
	return -1
}
