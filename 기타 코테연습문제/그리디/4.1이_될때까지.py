"""
자연수 N이 1이 될때까지 K 로나누거나, 1 빼는 과정 반복하기, 최소 횟수 구하기
# N을 K의 배수로 만들어서 나누는 방식 사용
25 5
결과 : 2
"""


def solution():
    count = 0
    N, K = map(int, input().split())
    while True:
        target = (N // K) * K
        count += N - target
        N = target
        N //= K  # 나누기
        count += 1
        if N < K:
            count += N - 1
            break
    return count


if __name__ == "__main__":
    print(solution())
