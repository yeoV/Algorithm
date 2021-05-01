
def solution(s):
    stack = []
    dic = {'(': ')', '[': ']', '{': '}'}
    if len(s) % 2 != 0:
        return False
    else:
        for i in s:
            if i in dic.keys():
                stack.append(i)
                # print(stack)
            else:
                if stack:
                    tmp = stack.pop(-1)
                    if i == dic[tmp]:
                        continue
                    else:
                        # print('false')
                        return False
                else:
                    # print('false')
                    return False
        # print('true')
        return True


solution("{{}}")
solution("[")
solution("({})[]")
solution("[)")
solution("]()[")
solution("([())]")
solution("[{[{[]}]}]")
