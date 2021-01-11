'''
DFS로 문제 해결
4 5
00110
00011
11111
00000
결과 -> 3
'''
n, m = map(int, input().split(' '))

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# 방문처리 방법 -> 0을 1로 변경해줌
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 -> False 반환
    # -1 인 경우도 반드시 예외 처리 해주어야 함
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 방문하지 않았다면, 상하좌우 모두 방문
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        # if i == 0 and j == 4:
        #     print("!")
        if dfs(i, j) == True:
            print(i, j)
            result += 1
print(result)
