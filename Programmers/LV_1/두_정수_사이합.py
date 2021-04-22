def solution(a, b):

    tmp = list(range(a, b + 1)) if a < b else list(range(b, a + 1))
    print(sum(tmp))


solution(5, 1)
solution(3, 5)
solution(3, 3)


# 합 공식 이용
def solution2(a, b):
    print(((abs(a - b) + 1) * (a + b)) // 2)


solution2(5, 1)
solution2(3, 5)
solution2(3, 3)
