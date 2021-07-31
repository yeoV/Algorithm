# https://www.acmicpc.net/problem/14621
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n, m = map(int, read().split())
node = [i for i in range(n + 1)]
sex = read().split()
edge = []
for _ in range(m):
    a, b, w = map(int, read().split())
    heappush(edge, (w, a, b))


def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        node[b] = a
    else:
        node[a] = b


def find(x):
    if node[x] == x:
        return x
    # 경로 압축
    node[x] = find(node[x])
    return node[x]


# 크루스칼
def run(edge):
    ans = 0
    count = 0
    while edge:
        w, a, b = heappop(edge)
        # 서로소가 아니고 node 성별이 같은 경우는 무시
        if find(a) == find(b) or sex[a - 1] == sex[b - 1]:
            continue
        union(a, b)
        ans += w
        count += 1
        # 모두 연결했을 경우 -> 간선최대 : n - 1
        if count == n - 1:
            return count, ans

    return count, ans


count, ans = run(edge)
if count != n - 1:
    print(-1)
else:
    print(ans)
