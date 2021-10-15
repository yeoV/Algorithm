# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter
import math


def parsing(str):
    arr = []
    for i in range(len(str) - 1):
        tmp = str[i : i + 2]
        if tmp.isalpha():
            arr.append(tmp.lower())
    return arr


def solution(str1, str2):
    arr1 = Counter(parsing(str1))
    arr2 = Counter(parsing(str2))
    union = sum((arr1 | arr2).values())
    intersection = sum((arr1 & arr2).values())
    try:
        ans = int((intersection / union) * 65536)
    except ZeroDivisionError:
        ans = 65536
    print(ans)
    return ans


solution("FRANCE", "french")
solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")
solution("E=M*C^2", "e=m*c^2")
