def solution(d, budget):
    cnt = 0
    d.sort()
    for val in d:
        budget -= val
        if budget < 0:
            break
        cnt += 1
    return cnt


solution([1, 3, 2, 5, 4], 9)
solution([2, 2, 3, 3], 10)
