def solution(no, works):
    answer = 0
    works.sort(reverse=True)

    while no > 0 and works[0] > 0:
        cnt = works.count(works[0])

        for i in range(cnt):
            if no > 0:
                works[i] -= 1
                no -= 1
            else:
                break
    answer = sum([i**2 for i in works])
    return answer


solution(4, [4, 3, 3])
