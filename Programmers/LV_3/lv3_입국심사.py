# https://programmers.co.kr/learn/courses/30/lessons/43238

INF = float("inf")


def solution(n, times):
    s, e = 0, times[-1] * n

    while s <= e:
        mid = (s + e) // 2

        if sum([mid // time for time in times]) >= n:
            e = mid - 1
        else:
            s = mid + 1
        # 사람 수요가 가능한지 검사
    print(s)


solution(6, [7, 10])
