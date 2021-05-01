

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
#     if numbers[0] == '0':
#         answer = '0'
#     else:
#         answer = ''.join(numbers)
#     return answer


# solution([6, 10, 2])


def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=lambda x: (x*4)[:4], reverse=True)
    if numbers[0] == '0':
        return '0'
    else:
        return "".join(numbers)


solution([3, 30, 34, 5, 9])
