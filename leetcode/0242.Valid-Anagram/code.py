from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        return all(s[x] == t[x] for c in (s, t) for x in c)        

if __name__ == "__main__":
    print(Solution().isAnagram("hello", "hallo"))
    print(Solution().isAnagram("a", "abb")) # return False
    