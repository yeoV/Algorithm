def solution(board, nums):
    # N x N 빙고판에서 빙고가 나오기 위해서는 N개의 원소가 필요
    size = len(board)   # 빙고판의 사이즈 N
    hor = [0] * size    # 가로 몇번 나왔는지
    ver = [0] * size    # 세로 몇번 나왔는지
    diag = [0] * 2      # 대각선은 2개 뿐
    idx = {}

    # 빙고에서 중요한건 결국 인덱스
    # 2중 루프 board -(x,y) 대응관계 넣기
    for x in range(size):
        for y in range(size):
            idx[board[x][y]] = (x, y)

    # 'num'을 순회
    for num in nums:
        # 둘의 순서를 바꿔야 함
        y, x = idx[num]
        if x == y:
            diag[0] += 1
        if y == size - x - 1:
            diag[1] += 1
        hor[x] += 1
        ver[y] += 1

    # counting 작업이 필요

    return hor.count(size) + ver.count(size) + diag.count(size)


solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [
         5, 14, 6, 9]],	[14, 3, 2, 4, 13, 1, 16, 11, 5, 15])
