# https://www.acmicpc.net/problem/3079
import sys

read = sys.stdin.readline
MAX_TIME = 10 ** 18

n, m = map(int, read().split())
time_table = [int(read().rstrip()) for i in range(n)]
s, e = 1, MAX_TIME


def check(mid):
    flag = sum(mid // x for x in time_table)
    if flag >= m:
        return True
    return False


while s <= e:
    mid = (s + e) // 2

    if check(mid):
        e = mid - 1
    else:
        s = mid + 1
print(s)
