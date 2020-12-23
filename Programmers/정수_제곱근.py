import math


def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return (math.sqrt(n) + 1) ** 2
    else:
        return -1


# is_integer 활용
def solution2(n):
    print((math.sqrt(n) + 1) ** 2 if math.sqrt(n).is_integer() else -1)


solution2(121)
solution2(114)
