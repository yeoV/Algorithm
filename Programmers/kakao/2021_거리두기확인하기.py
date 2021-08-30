# https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque


def check_distance(students, graph):
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visit = [[False] * 5 for _ in range(5)]
    for student in students:
        q = deque([student])
        visit[student[0]][student[1]] = True

        while q:
            x, y, dist = q.popleft()
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                nxt_dist = dist + 1
                if nxt_dist <= 2:
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visit[nx][ny]:
                        if graph[nx][ny] == 'O':
                            visit[nx][ny] = True
                            q.append((nx, ny, nxt_dist))
                        elif graph[nx][ny] == 'P':
                            return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        student = []
        for row, seat in enumerate(place):
            for col, val in enumerate(seat):
                if val == 'P':
                    student.append((row, col, 0))
        answer.append(check_distance(student, place))
    # print(answer)
    return answer


# solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]])
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
