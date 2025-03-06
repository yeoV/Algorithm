package leetcode

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	alpa := make([]int, 26)

	for _, v := range s {
		alpa[v-'a'] += 1
	}
	for _, v := range t {
		alpa[v-'a'] -= 1
	}

	for _, v := range alpa {
		if v != 0 {
			return false
		}
	}
	return true
}
