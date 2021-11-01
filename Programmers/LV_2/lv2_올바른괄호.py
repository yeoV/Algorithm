def solution(s):
    stack = []
    dic = {'(': ')'}
    if len(s) % 2 != 0:
        return False
    else:
        for val in s:
            if val in dic.keys():
                stack.append(val)
            else:
                if stack:
                    key = stack.pop(-1)
                    if dic[key] == val:
                        continue
                    else:
                        return False
                else:
                    return False
        # 모든 괄호 진행 후 스택이 비어있지 않을 경우
        if stack:
            return False
        else:
            return True


solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")
