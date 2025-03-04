package leetcode

// Beats 100%
func findTheDifference(s string, t string) byte {
	count := make(map[rune]int)
	var res byte
	for _, v := range s {
		count[v] = count[v] + 1
	}
	for _, v := range t {
		if count[v] > 0 {
			count[v] = count[v] - 1
		} else {
			res = byte(v)
		}
	}
	return res
}
