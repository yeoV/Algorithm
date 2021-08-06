# https://www.acmicpc.net/problem/1976
import sys

read = sys.stdin.readline
n = int(read().rstrip())
m = int(read().rstrip())
edges = []
node = [i for i in range(n)]


def find(a):
    if node[a] == a:
        return a
    node[a] = find(node[a])
    return node[a]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        node[y] = x
    else:
        node[x] = y


# O(n^2)
for i in range(n):
    tmp = list(map(int, read().split()))
    for j, val in enumerate(tmp):
        if val == 1:
            # 결합
            if find(i) != find(j):
                union(i, j)


trip = list(map(int, read().split()))
first = find(trip[0] - 1)
for k in trip[1:]:
    tmp = find(k - 1)
    if tmp != first:
        print("NO")
        break
else:
    print("YES")
