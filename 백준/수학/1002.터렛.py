import math
T = int(input())


def distance(x1, x2, y1, y2, r1, r2):
    dis = math.sqrt((x1 - x2)**2 + (y1 - y2) ** 2)
    rs = abs(r1 - r2)
    rm = r1+r2
    if dis == 0:
        # 아예 일치하는 경우
        if r1 == r2:
            print(-1)
        # 포함하고 있는 겨웅
        else:
            print(0)
    # 한 점만 겹침
    else:
        if rs == dis or rm == dis:
            print(1)
        # 2점이 겹침
        elif rs < dis < rm:
            print(2)
        else:
            print(0)


for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance(x1, x2, y1, y2, r1, r2)
