from heapq import heappush, heappop, heapify


def solution(scoville, K):
    ans = 0
    heapify(scoville)
    while True:
        try:
            if scoville[0] < K:
                heappush(scoville, heappop(scoville) + heappop(scoville)*2)
                ans += 1
            else:
                break
        except IndexError:
            return -1

    # print(scoville)
    # print(ans)
    return ans


solution([1, 2, 3], 20)
# solution([1, 2, 3, 9, 10, 12], 7)
# solution([2, 1, 3, 0], 5)
# solution([6, 1, 3, 2], 30)
