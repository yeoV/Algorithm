# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    ans = new_id.lower()  # 1 단계
    ans = re.sub('[^a-z0-9-_.]',"", ans)  # 2 단계
    # 3단계
    ans = re.sub('\.+', '.', ans)
    # 4단계
    ans = ans.strip('.')
    # 5 단계
    ans = "a" if not ans else ans
    # 6 단계
    ans = ans[:15] if len(ans) >= 16 else ans
    ans = ans.rstrip('.')
    # 7단계
    while len(ans) < 3:
        ans += ans[-1]
    # print(ans)
    return ans


solution("...!@BaT#*..y.abcdefghijklm")
