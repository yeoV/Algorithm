# https://www.acmicpc.net/problem/2667
import sys
read = sys.stdin.readline
N = int(input())
vector = ((-1, 0), (1, 0), (0, 1), (0, -1))  # 상 하 좌 우
count = 0
house_map = []
result = []
for _ in range(N):
    house_map.append(list(map(int, read().rstrip())))


def dfs(house_map, location):
    global count
    row, col = location
    if 0 <= row and row < N and 0 <= col and col < N:
        if house_map[row][col] == 1:
            house_map[row][col] = 0
            count += 1
            dfs(house_map, (row + vector[0][0], col + vector[0][1]))
            dfs(house_map, (row + vector[1][0], col + vector[1][1]))
            dfs(house_map, (row + vector[2][0], col + vector[2][1]))
            dfs(house_map, (row + vector[3][0], col + vector[3][1]))
            return True
    else:
        return False


for row in range(N):
    for col in range(N):
        if house_map[row][col] == 1:
            dfs(house_map, (row, col))
            result.append(count)
            count = 0
result.sort()
print(len(result))
for i in result:
    print(i, end="\n")
