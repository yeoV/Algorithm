from itertools import combinations
import sys
read = sys.stdin.readline
N = int(input())
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i] = [0] + list(map(int, read().split()))

for i in range(1, N+1):
    for j in range(1, N+1):
        if i <= j:
            graph[i][j] = graph[i][j] + graph[j][i]
team1_list = list(combinations(range(1, N+1), N//2))
team1_list = team1_list[:int(len(team1_list)/2)]
ans = int(1e9)
for team1 in team1_list:
    team1_score, team2_score = 0, 0
    team2 = set(range(1, N+1)) - set(team1)
    for i, j in combinations(team1, 2):
        team1_score += graph[i][j]
    for i, j in combinations(team2, 2):
        team2_score += graph[i][j]
    ans = min(ans, abs(team1_score - team2_score))
print(ans)

# import sys

# input = sys.stdin.readline


# def dfs(idx, cnt):
#     global ans
#     if cnt == n // 2:
#         start, link = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if select[i] and select[j]:
#                     print(f'start 팀{i}, {j}')
#                     start += a[i][j]
#                 elif not select[i] and not select[j]:
#                     print(f'link 팀{i}, {j}')
#                     link += a[i][j]
#         print(f'start 대 link {start}, {link}')
#         ans = min(ans, abs(start - link))
#     for i in range(idx, n):
#         if select[i]:
#             continue
#         select[i] = 1
#         print(select, i)
#         dfs(i + 1, cnt + 1)
#         select[i] = 0


# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# select = [0 for _ in range(n)]
# ans = sys.maxsize
# dfs(0, 0)
# print(ans)
