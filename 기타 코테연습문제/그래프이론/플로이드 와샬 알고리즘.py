
n = 4
graph = [
    [0, 5, float('inf'), 8],
    [7, 0, 9, float('inf')],
    [2, float('inf'), 0, 4],
    [float('inf'), float('inf'), 3, 0]
]
res = list.copy(graph)


def floydWarshall(graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])
    print(res)


floydWarshall(graph)
