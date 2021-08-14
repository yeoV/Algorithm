# https://www.acmicpc.net/problem/1939
import sys
from collections import deque
read = sys.stdin.readline
n, m = map(int, read().split())
islands = [[] for _ in range(n+1)]
MAX = 0
for _ in range(m):
    a, b, c = map(int, read().split())
    MAX = max(MAX, c)
    islands[a].append((b, c))
    islands[b].append((a, c))

start, target = map(int, read().split())
# 다리 건널 수 있는지
def check(max_w):
    q = deque([start])
    visit = [False] * (n+1)
    while q:
        node = q.popleft()
        if node == target:
            return True
        for nxt_node, w in islands[node]:
            if not visit[nxt_node] and w >= max_w:
                visit[nxt_node] = True
                q.append(nxt_node)
    return False

# 최대 무게 이분탐색
s, e = 0, MAX
while s <= e:
    mid = (s + e) // 2
    if check(mid):
        s = mid + 1
    else:
        e = mid - 1

print(e)


