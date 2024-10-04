# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    answer = 1e9
    q = deque()
    len_x, len_y = len(maps), len(maps[0])
    visited = [[False for _ in range(len_y)] for _ in range(len_x)]
    dxy = [(0,-1), (0,1), (-1,0), (1,0)]
    
    # 시작 부분
    q.append((0,0,1))
    visited[0][0] = True
    
    # q가 존재하는 경우
    while q:
        x, y, val = q.popleft()
        
        # 맨 우측 하단
        if (x,y) == (len_x -1, len_y-1):
            answer = min(answer, val)
            continue
        
        # 4방향 검사
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # 벽 나가는 경우
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,val + 1))
    
    return answer if answer != 1e9 else -1