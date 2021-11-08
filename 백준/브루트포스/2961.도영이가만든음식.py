# https://www.acmicpc.net/problem/2961
import sys


read = sys.stdin.readline
N = int(read().rstrip())
data = []
for _ in range(N):
    a, b = map(int, read().split())
    data.append((a, b))

ans = float("inf")


def run(depth, sour, bitter):
    global ans
    if depth == N:
        if (sour, bitter) != (1, 0):
            ans = min(ans, abs(sour - bitter))
        return
    # 포함하는 경우
    run(depth + 1, sour * data[depth][0], bitter + data[depth][1])
    # 포함 안하는 경우
    run(depth + 1, sour, bitter)


run(0, 1, 0)
print(ans)
