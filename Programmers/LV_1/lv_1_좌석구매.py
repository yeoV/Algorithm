def solution(seat):
    ans = set(map(tuple, seat))
    return len(ans)


solution([[1, 1], [2, 2], [3, 3]])
solution([[1, 1], [2, 1], [1, 2], [3, 4], [2, 1], [2, 1]])
