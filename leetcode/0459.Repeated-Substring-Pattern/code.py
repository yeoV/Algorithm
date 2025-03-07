class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        for i in range(1, len_s // 2 + 1):
            if len_s % i == 0:
                sub = s[:i]
                if sub * (len_s // i) == s:
                    return True
                
        return False
if __name__ == "__main__":
    Solution().repeatedSubstringPattern("abab")
    Solution().repeatedSubstringPattern("abcabcabc")
    Solution().repeatedSubstringPattern("aba")