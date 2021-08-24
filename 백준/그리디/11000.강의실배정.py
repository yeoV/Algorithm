# https://www.acmicpc.net/problem/11000
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n = int(read().rstrip())
times = [tuple(map(int, read().split())) for _ in range(n)]
times.sort()
room = []

# 끝나는 시간 저장
heappush(room, times[0][1])

for time in times[1:]:
    if time[0] < room[0]:
        heappush(room, time[1])
    else:
        heappop(room)
        heappush(room, time[1])
print(len(room))