# https://www.acmicpc.net/problem/16562
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
friends = list(map(int, read().split()))
parent = [[i, friends[i-1]] for i in range(n+1)]
# 친구비는 랭크 개념을 도입하면 어떨련지
def find(x):
    if parent[x][0] == x:
        return x
    parent[x][0] = find(parent[x][0])
    return parent[x][0]

def union(x, y):
    x = find(x)
    y = find(y)
    # 친구비가 더 작은 아이를 부모로 연결
    if parent[x][1] > parent[y][1]:
        parent[x][0] = parent[y][0]
    elif parent[x][1] < parent[y][1]:
        parent[y][0] = parent[x][0]
    else:
        parent[y][0] = parent[x][0]

for _ in range(m):
    a, b = map(int, read().split())
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)
for idx in range(1, n):
    find(idx)
parent_set = set(map(lambda x: x[0], parent[1:]))
total_fee = sum(map(lambda x : friends[x-1], parent_set))
print(total_fee) if not total_fee > k else print('Oh no')