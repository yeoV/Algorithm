# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
read = sys.stdin.readline
# 임의의 두 칸 (r1, c1)과 (r2, c2),  |r1-r2| + |c1-c2| 치킨거리
n, m = map(int, read().split())
city = []
chickens = []
houses = []
for i in range(n):
    city.append(list(map(int, read().split())))
    for j, val in enumerate(city[i]):
        if val == 2:
            chickens.append((i, j))
        elif val == 1:
            houses.append((i, j))


# 도시의 치킨 거리 -> 모든 집과 치킨 가게와의 거리의 합
res = float('inf')
for chicken in combinations(chickens, m):
    dist = 0
    for house in houses:
        tmp = float('inf')
        for c in chicken:
            # 각각 집까지의 거리를 계산
            tmp = min(tmp, abs(c[0] - house[0]) + abs(c[1] - house[1]))
        dist += tmp
    res = min(res, dist)
print(res)
