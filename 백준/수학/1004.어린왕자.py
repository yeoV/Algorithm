import math
T = int(input())
ans = 0


def distance(x1, y1, val):
    cx, cy, r = val
    dis = math.sqrt((x1-cx) ** 2 + (y1-cy)**2)
    if dis < r:
        return True
    else:
        return False


for _ in range(T):
    start, end = False, False
    ans = 0
    arr = []
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    for _ in range(n):
        val = tuple(map(int, input().split()))
        # 어린왕자 위치 기준
        start = distance(x1, y1, val)
        # 도착 위치 기준
        end = distance(x2, y2, val)
        if start and end:
            continue
        elif start or end:
            ans += 1
        else:
            continue
    print(ans)
