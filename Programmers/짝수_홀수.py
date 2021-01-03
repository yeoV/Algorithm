'''
짝수 일 경우, even 홀수 odd 반환
'''


def solution(num):
    # return "Even" if num % 2 == 0 else "Odd"
    return (num % 2 and "Odd") or 'Even'


if __name__ == "__main__":
    print(solution(3))
    print(solution(4))
