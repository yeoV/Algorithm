
def solution(monster, S1, S2, S3):
    all_cases = S1*S2*S3
    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                if i+j+k+1 in monster:
                    all_cases -= 1
    return int(all_cases / (S1*S2*S3) * 1000)


solution([4, 9, 5, 8], 2, 3, 4)
solution([4, 9, 5, 8], 2, 3, 3)
