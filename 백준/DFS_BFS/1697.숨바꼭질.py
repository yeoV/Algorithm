from collections import deque
import sys
read = sys.stdin.readline
N, K = map(int, read().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)


def bfs(start):
    q = deque([start])
    while q:
        loc = q.popleft()
        nxt = [loc+1, loc-1, loc*2]
        if loc == K:
            return dist[loc]
        for i in nxt:
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[loc] + 1
                q.append(i)


print(bfs(N))
