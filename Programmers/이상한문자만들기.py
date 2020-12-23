# 짝수번째 대문자, 홀수번째 소문자
from typing import List


def solution(s):
    answer = list()
    s = s.split()
    for words in s:
        tmp = ""
        for idx, word in enumerate(words):
            if idx % 2 == 0:
                tmp += word.upper()
            else:
                tmp += word.lower()
        answer.append(tmp)
    print(" ".join(answer))


solution("try hello world")


def solution2(s):
    print(
        " ".join(
            [
                "".join(
                    [v.upper() if i % 2 == 0 else v.lower() for i, v in enumerate(word)]
                )
                for word in s.split(" ")
            ]
        )
    )


solution2("try hello world")
