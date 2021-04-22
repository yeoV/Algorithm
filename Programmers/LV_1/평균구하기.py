# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 통계 모듈
import statistics


def solution(n):
    return sum(n) / len(n)


print(solution([1, 2, 3, 4]))


def solution2(list):
    return statistics.mean(list)


print(solution2([1, 2, 3, 4]))
