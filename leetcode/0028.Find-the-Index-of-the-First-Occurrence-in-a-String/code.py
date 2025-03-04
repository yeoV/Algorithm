class Solution:
    def __strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
    def _strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1


    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
         
        if m == 0:
            return 0
        bad_char = {needle[i]:i for i in range(m)}

        # 검색 시작
        i = 0
        while i <= n - m:
            j = m - 1

            # 뒤에서 부터 비교
            while j >= 0 and needle[j] == haystack[i+j]:
                j -= 1
            # 매칭 완료
            if j < 0:
                return i
            else:
                shift = j - bad_char.get(haystack[i + j], -1)
                i += max(1, shift)  # 최소 1 이상 이동
         
        return -1

if __name__ == "__main__":
    print(Solution().strStr("sadbutsad", "sad"))
    print(Solution().strStr("leetcode", "leeto"))