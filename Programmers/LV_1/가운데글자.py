def solution(text):
    tmp = len(text)
    idx = int(tmp / 2)
    if tmp / 2 == idx:
        return text[idx - 1 : idx + 1]
    else:
        return text[idx]


solution("abc")
solution("abcd")


def string_middle(text):
    print(text[(len(text) - 1) // 2 : len(text) // 2 + 1])


string_middle("abc")
string_middle("abcdef")

