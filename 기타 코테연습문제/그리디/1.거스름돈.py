# 거스름돈을 가장 최소의 갯수로 걸러주기
# 가장 큰 단위는 작은 단위의 배수
def solution(N):
    coins = (500, 100, 50, 10)
    count = 0
    for coin in coins:
        count += N // coin
        N %= coin
    return count


if __name__ == "__main__":
    print(solution(1260))
