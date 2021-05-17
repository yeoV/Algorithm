from itertools import combinations


def solution(m, weights):
    answer = 0
    for i in range(1, len(weights)):
        for comb in combinations(weights, i):
            if sum(comb) == m:
                answer += 1
    return answer


solution(3000, [500, 1500, 2500, 1000, 2000])
