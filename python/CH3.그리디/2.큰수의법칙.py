#  5 8 3, 2 4 5 4 6 입력
# 46 출력
#


def solution():
    n, m, k = map(int, input().split(" "))
    arr = list(map(int, input().split()))

    arr.sort()
    fir_num = arr[-1]
    Sec_num = arr[-2]
    res, count = 0, 0
    for _ in range(m):
        if count == k:
            res += Sec_num
            count = 0
            continue
        res += fir_num
        count += 1
    return res


# 가장 큰 수와 두번째 큰수를 하나의 배열로 생각해서 해결
def solution2():
    n, m, k = map(int, input().split(" "))
    arr = list(map(int, input().split()))

    arr.sort()
    fir_num = arr[-1]
    Sec_num = arr[-2]
    res, count = 0, 0
    count += (m // (k + 1)) * k
    count += m % (k + 1)

    res += count * fir_num
    res += (m - count) * Sec_num
    return res


if __name__ == "__main__":
    print(solution())
    print(solution2())
