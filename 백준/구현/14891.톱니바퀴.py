# https://www.acmicpc.net/problem/14891
import sys
from collections import deque
read = sys.stdin.readline

# 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
gears = deque(deque(map(int, read().rstrip())) for _ in range(4))
k = int(read().rstrip())
# print(gears)

def check_right(gear, direction):
    # 범위를 벗어나거나 같은 경우 stop
    if gear >= 3 or gears[gear][2] == gears[gear + 1][6]:
        return

    check_right(gear + 1, -direction)
    gears[gear+1].rotate(-direction)

def check_left(gear, direction):
    if gear <= 0 or gears[gear][6] == gears[gear - 1][2]:
        return
    check_left(gear - 1, -direction)
    gears[gear-1].rotate(-direction)


while k:
    gear, direction = map(int, read().split())
    gear -= 1
    check_right(gear, direction)
    check_left(gear, direction)
    gears[gear].rotate(direction)
    k -= 1

ans = 0
for i in range(4):
    ans += 0 if gears[i][0] == 0 else 1 << i
print(ans)