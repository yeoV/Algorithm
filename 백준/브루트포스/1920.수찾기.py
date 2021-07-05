# https://www.acmicpc.net/problem/1920
import sys
read = sys.stdin.readline
n = int(read().rstrip())
A = dict()
for val in map(int, read().split()):
    A[val] = 1
m = int(read().rstrip())
for val in map(int, read().split()):
    try:
        print(A[val])
    except KeyError:
        print(0)
