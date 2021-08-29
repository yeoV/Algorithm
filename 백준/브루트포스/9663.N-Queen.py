# https://www.acmicpc.net/problem/9663
import sys
read = sys.stdin.readline
n = int(read().rstrip())
cols = [-1 for _ in range(n)]
res = 0


def promise(row, col):
    if cols[col] != -1:
        return False
    # 대각선 검사
    for i in range(n):
        # 이미 있는 퀸중에 대각선에 있는 경우
        if cols[i] != -1 and abs(cols[i] - row) == abs(i - col):
            return False
    return True


def find_queen(d):
    global res
    if d == n:
        res += 1
        return

    for i in range(n):
        if promise(d, i):
            cols[i] = d
            find_queen(d+1)
            cols[i] = -1


find_queen(0)
print(res)
