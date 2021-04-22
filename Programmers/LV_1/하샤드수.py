def solution(x):
    num = x
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return True if (num/sum) == int(num/sum) else False


print(solution(12))


'''
각 자리수의 합을 구할 경우, str을 이용하면 편리함.
'''


def solution2(x):
    # print(sum([int(c) for c in str(x)]))
    return x % sum([int(c) for c in str(x)]) == 0


print(solution2(12))
print(solution2(11))
print(solution2(15))
