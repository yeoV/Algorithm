
def solution(s):
    ans = len(s)

    for step in range(1, ans // 2 + 1):
        compressed = ''
        prev = s[0:step]
        cnt = 1
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                cnt += 1
            else:
                compressed += (str(cnt) + prev) if cnt > 1 else prev
                prev = s[i:i+step]
                cnt = 1
        compressed += (str(cnt) + prev) if cnt > 1 else prev
        print(compressed)
        ans = min(ans, len(compressed))
    print(ans)
    return ans

solution("aabbaccc")
# solution("ababcdcdababcdcd")
# solution("abcabcdede")
# solution("abcabcabcabcdededededede")
# solution("xababcdcdababcdcd")
