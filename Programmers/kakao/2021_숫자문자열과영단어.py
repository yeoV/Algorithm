# https://programmers.co.kr/learn/courses/30/lessons/81301

mapping = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}


# 내가 처음 푼 풀이
def solution1(s):
    ans, key = "", ""
    for idx in range(len(s)):
        if s[idx].isnumeric():
            ans += s[idx]
        else:
            key += s[idx]
            try:
                ans += mapping[key]
                key = ""
            except KeyError:
                continue
    # print(int(ans))
    return int(ans)


# 더 깔끔한 풀이
def solution2(s):
    ans = s
    for k, v in mapping.items():
        ans = ans.replace(k, v)
    # print(ans)
    return int(ans)


solution1("one4seveneight")
