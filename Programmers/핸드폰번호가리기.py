def solution(phone_number):
    stars = '*' * len(phone_number[:-4])
    return stars + phone_number[-4:]


print(solution("01012344444"))
