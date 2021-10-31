# https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque


def bfs(start, computers, visit):
    q = deque([])
    q.append(start)
    while q:
        node = q.popleft()

        for nxt_n, val in enumerate(computers[node]):
            if not visit[nxt_n] and val == 1:
                visit[nxt_n] = True
                q.append(nxt_n)


def solution(n, computers):
    ans = 0
    visit = [False] * n
    for idx in range(n):
        if not visit[idx]:
            visit[idx] = True
            ans += 1
            bfs(idx, computers, visit)
    print(ans)
    return ans

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
