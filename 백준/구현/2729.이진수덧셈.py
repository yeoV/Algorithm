# https://www.acmicpc.net/problem/2729
import sys

read = sys.stdin.readline

n = int(read().rstrip())

for _ in range(n):
    n1, n2 = read().split()
    # format() -> 이용하여 접두어 제거 가능
    ans = format(int(n1, 2) + int(n2, 2), "b")
    print(ans)
