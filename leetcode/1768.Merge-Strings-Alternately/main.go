package algo

import "strings"

// func mergeAlternately(word1 string, word2 string) string {
// 	var res strings.Builder
// 	len1, len2 := len(word1), len(word2)
// 	for i := 0; i < max(len1, len2); i++ {
// 		if i < len1 {
// 			res.WriteByte(word1[i])
// 		}
// 		if i < len2 {
// 			res.WriteByte(word2[i])
// 		}
// 	}
// 	return res.String()
// }

func mergeAlternately(word1 string, word2 string) string {
	var res strings.Builder
	len1, len2 := len(word1), len(word2)

	res.Grow(len1 + len2)
	i := 0
	for ; i < len1 && i < len2; i++ {
		res.WriteByte(word1[i])
		res.WriteByte(word2[i])
	}
	if i < len1 {
		res.WriteString(word1[i:])
	}
	if i < len2 {
		res.WriteString(word2[i:])
	}
	return res.String()
}
