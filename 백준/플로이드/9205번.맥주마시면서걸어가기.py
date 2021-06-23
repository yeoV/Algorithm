import sys
read = sys.stdin.readline
test_case = int(input())
ans = list()


def distance(start, end):
    dis = abs(start[0] - end[0]) + abs(start[1] - end[1])
    if dis <= 1000:
        return True
    else:
        return False


while test_case > 0:
    N = int(input())
    node = [0] * (N + 2)
    dis = [[False] * (N+2) for _ in range(N+2)]
    for i in range(N+2):
        node[i] = (tuple(map(int, read().split())))
    for i in range(N+2):
        for j in range(N+2):
            dis[i][j] = distance(node[i], node[j])
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                # 왜이부분이 오류..?
                if (dis[i][k] and dis[k][j]) or dis[i][j]:
                    dis[i][j] = True

    if dis[-1][0]:
        ans.append('happy')
    else:
        ans.append('sad')
    test_case -= 1
for val in ans:
    print(val)
