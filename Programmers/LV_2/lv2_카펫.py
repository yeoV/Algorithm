def solution(brown, red):
    total = brown + red
    for i in range(2, total):
        if total % i == 0:
            j = total // i
            if red == (i - 2) * (j - 2):
                return [j, i]


solution(10, 2)
solution(8, 1)
solution(24, 24)
