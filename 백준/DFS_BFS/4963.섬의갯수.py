'''
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
3
'''
graph, answer = [], []
w, h, result = 0, 0, 0
vector = {(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= h or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i, j in vector:
            dfs(x+i, y+j)
        return True
    return False


while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
            if dfs(x, y):
                result += 1
    answer.append(result)
    result = 0
    graph = []
print(*answer, sep='\n')
