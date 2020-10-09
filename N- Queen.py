def dfs(depth):
    global cnt
    if depth is n:
        cnt += 1

    else:  # 분기문
        for i in range(1, n + 1):
            if promise(depth + 1, i):
                # 상태저장
                cols[i] = depth + 1
                dfs(depth + 1)
                # 상태되돌리기
                cols[i] = 0


def promise(row, col):
    # 같은 열에 위치하는가
    if cols[col] != 0:
        return False

    for i in range(1, n + 1):
        if cols[i] != 0 and abs(cols[i] - row) == abs(i - col):
            return False
    return True


n = int(input("n값: "))
cols = [0 for _ in range(n + 1)]
print(cols)
cnt = 0
dfs(0)
print(cnt)
