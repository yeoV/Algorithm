"""
N x M 개의 카드 형식, 각 행마다 가장 작은 숫자 중 가장 큰 값 반환
3 3
3 1 2
4 1 4
2 2 2
결과 2
"""


def solution():
    result = 0
    N, M = map(int, input().split())
    for _ in range(N):
        cards = list(map(int, input().split()))
        min_val = min(cards)
        result = max(result, min_val)
    return result


if __name__ == "__main__":
    print(solution())
