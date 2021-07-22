# https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline
n, m = map(int, read().split())
# 첫번째는 idx, 2번째는 rank
p = [[i, 0] for i in range(n + 1)]


def find(idx):
    if p[idx][0] == idx:
        return idx
    p[idx][0] = find(p[idx][0])
    return p[idx][0]


def union(a, b):
    # rank system 적용
    # 랭크가 더 큰쪽이 부모노드가 됨
    if p[a][1] > p[b][1]:
        p[b][0] = a
    elif p[a][1] < p[b][1]:
        p[a][0] = b
    else:
        p[a][1] += 1
        p[a][0] = b


for _ in range(m):
    a, b, c = map(int, read().split())
    b, c = find(b), find(c)
    if a:
        print('YES' if b == c else 'NO')
    else:
        # 같은 경우에는 union할 필요없음
        if b != c:
            union(b, c)
