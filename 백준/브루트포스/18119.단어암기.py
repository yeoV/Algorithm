"""
https://www.acmicpc.net/problem/18119
"""
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
words = []
forgot = 0
for _ in range(n):
    tmp = 0
    for w in read().rstrip():
        w = 1 << ord(w) - ord('a')
        tmp |= w
    words.append(tmp)
for _ in range(m):
    cnt = 0
    o, w = read().split()
    if o == '1':
        forgot |= 1 << ord(w) - ord('a')
    else:
        forgot -= 1 << ord(w) - ord('a')
    for word in words:
        if word & forgot == 0:
            cnt += 1
    print(cnt)
