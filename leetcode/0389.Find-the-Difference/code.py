class Solution:
    # 3ms, 53% Beats
    def _findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for idx in range(min(len(s), len(t))):
            if s[idx] != t[idx]:
                return t[idx]
        return t[-1]
    
    # XOR!
    def findTheDifference(self, s: str, t: str) -> str:
        from functools import reduce
        from operator import xor
        return chr(reduce(xor, map(ord, s + t)))


    

# 같은 단어가 있을 수 있다
if __name__ == "__main__":
    print(Solution().findTheDifference("abcd","abcde"))
    print(Solution().findTheDifference("a","aa"))