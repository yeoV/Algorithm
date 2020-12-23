def solution(n):
    print(list(map(int, reversed(str(n)))))


solution(12345)


def solution2(n):
    print([int(x) for x in str(n)][::-1])


solution2(12345)
