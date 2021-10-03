# https://www.acmicpc.net/problem/18222
import sys

read = sys.stdin.readline
k = int(read().rstrip())


def run(n):
    if n == 1:
        return 0
    prev = 1
    while (prev * 2) < n:
        prev *= 2
    return 1 - run(n - prev)


print(run(k))
