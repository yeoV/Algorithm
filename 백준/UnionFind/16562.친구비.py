# https://www.acmicpc.net/problem/16562
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
cost = [0] + list(map(int, read().split()))
nodes = [i for i in range(n+1)]
# 친구비는 랭크 개념을 도입하면 어떨련지
def find(x):
    if nodes[x] == x:
        return x
    nodes[x] = find(nodes[x])
    return nodes[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if cost[x] > cost[y]:
        nodes[x] = y
    elif cost[y] > cost[x]:
        nodes[y] = x
    else:
        nodes[x] = y

for _ in range(m):
    a, b = map(int, read().split())
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)

fee = 0
for idx in range(1,n+1):
    if idx == nodes[idx]:
        fee += cost[idx]
print(fee if fee <= k else 'Oh no')