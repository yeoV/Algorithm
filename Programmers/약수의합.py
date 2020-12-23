def solution(n):
    tmp = [x for x in range(1, n + 1) if n % x == 0]
    print(sum(tmp))


solution(12)
solution(32)


def solution2(n):
    tmp = [x for x in range(1, (n // 2) + 1) if n % x == 0]
    print(sum(tmp) + n)


solution2(12)
solution2(32)
