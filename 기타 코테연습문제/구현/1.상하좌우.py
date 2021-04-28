'''
1,1 좌표 부터 시작해서 plan에 맞는 위치로 이동
이동 5
R R R U D D
결과 3 4
'''


def solution():
    N = int(input())
    x, y = 1, 1
    plans = input().split()
    move_types = ['L', 'R', 'U', 'D']
    # L, R, U, D
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for plan in plans:
        nx, ny = move[move_types.index(plan)]
        nx = x + nx
        ny = y + ny
        if 0 in (nx, ny):
            continue
        x, y = nx, ny
    return f"{x} {y}"


if __name__ == "__main__":
    print(solution())
