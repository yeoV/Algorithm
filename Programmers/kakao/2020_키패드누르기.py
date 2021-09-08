# https://programmers.co.kr/learn/courses/30/lessons/67256
keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2),
          '*': (3, 0), 0: (3, 1), '#': (3, 2)}


def precision(left, right, next, hand):
    left, right, next = keypad[left], keypad[right], keypad[next]
    left_dis = abs(left[0] - next[0]) + abs(left[1] - next[1])
    right_dis = abs(right[0] - next[0]) + abs(right[1] - next[1])
    if left_dis < right_dis:
        return 'L'
    elif left_dis > right_dis:
        return 'R'
    else:
        return 'L' if hand == 'left' else 'R'


def solution(numbers, hand):
    answer = []
    left, right = '*', '#'
    for number in numbers:
        if number in {1, 4, 7}:
            answer.append('L')
            left = number
        elif number in {3, 6, 9}:
            answer.append('R')
            right = number
        else:
            tmp = precision(left, right, number, hand)
            answer.append(tmp)
            if tmp == 'L':
                left = number
            else:
                right = number
    return "".join(answer)


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
