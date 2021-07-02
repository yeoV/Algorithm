# https://www.acmicpc.net/problem/2504
import sys
read = sys.stdin.readline
bracket = read().rstrip()
s = []
tmp = 0
for b in bracket:
    tmp = 0
    if b == ')':
        while s and s[-1] != '(':
            e = s.pop()

            if type(e) == int:
                tmp += e
            else:
                print(0)
                exit()
        # 스택이 비어있는 경우
        if not s:
            print(0)
            exit()

        if not tmp:
            tmp = 1
        s.pop()
        s.append(tmp * 2)
    elif b == ']':
        while s and s[-1] != '[':
            e = s.pop()

            if type(e) == int:
                tmp += e
            else:
                print(0)
                exit()
        if not tmp:
            tmp = 1

        if not s:
            print(0)
            exit()

        s.pop()
        s.append(tmp * 3)
    else:
        s.append(b)
try:
    print(sum(s))
except TypeError:
    print(0)
