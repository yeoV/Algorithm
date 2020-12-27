"""
완전 탐색 -> 데이터가 100만개 이하인 경우에 실시
입력된 정수 N 까지의 시각 중 3이 하나라도 포함된 경우의 수

"""


def solution():
    N = int(input())
    count = 0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count


if __name__ == "__main__":
    print(solution())
