def solution(N, number):
    # 중복을 허용하지 않는 수
    answer = 0
    s = [set() for _ in range(8)]
    for i, x in enumerate(s, start=1):
        # 5, 55, 555 중복의 수
        x.add(int(str(N) * i))
    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer


solution(5, 12)
# solution(2, 11)
