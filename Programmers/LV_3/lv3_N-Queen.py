ans = 0


def promise(row, col, cols):
    # 이미 특정 열에 행의 정보가 담겨있음
    if cols[col] != -1:
        return False

    # 대각선 검사
    for idx, val in enumerate(cols):
        if cols[idx] != -1 and abs(val - row) == abs(idx - col):
            return False

    return True


def n_queen(d, n, cols):
    global ans
    # 종료 조건
    if d == n:
        ans += 1
        return

    # 값을 채울 반복문
    for col in range(n):
        # 백트래킹
        if promise(d, col, cols):
            cols[col] = d
            n_queen(d + 1, n, cols)
            cols[col] = -1
    return


def solution(n):
    # 1차원 배열 , cols -> 각각 열의 정보를 가지고 있음
    cols = [-1] * n

    n_queen(0, n, cols)
    print(ans)
    return ans


solution(4)
