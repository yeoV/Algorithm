import sys
read = sys.stdin.readline
R, C = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(R)]
move = ((0, 1), (0, -1), (1, 0), (-1, 0))


def dfs(depth, now, next):

    x, y = next
    for dxy in move:
        dx, dy = x+dxy[0], y+dxy[1]
        # 범위 검사 밑 같지 않은 알파벳일 경우
