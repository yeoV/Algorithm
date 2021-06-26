def solution(A, B):
    ans = 0
    A.sort()
    B.sort(reverse=True)
    for val in zip(A, B):
        ans += val[0] * val[1]
    return ans


solution([1, 4, 2], [5, 4, 4])
solution([1, 2], [3, 4])
