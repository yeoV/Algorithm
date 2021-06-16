"""
https://www.acmicpc.net/problem/1062 
"""
import sys
read = sys.stdin.readline
sys.setrecursionlimit(100)
N, K = map(int, read().split())
words = [read().rstrip() for _ in range(N)]
default = {'a', 'n', 't', 'i', 'c'}
max_cnt = 0


def dfs(d, start):
    global max_cnt
    if d == K - 5:
        cnt = 0
        # 단어 확인
        for word in words:
            for w in word:
                if w not in default:
                    break
            else:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        return
        # 반복문
    for i in range(start, ord('z') + 1):
        if chr(i) not in default:
            default.add(chr(i))
            dfs(d + 1, i + 1)
            default.remove(chr(i))


if K >= 5:
    dfs(0, ord('a'))
    print(max_cnt)
else:
    print(0)
