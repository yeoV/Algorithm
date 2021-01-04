'''
numpy 와 list 를 이용한 행렬의 덧셈 구현
'''
import numpy as np


def solution(A, B):
    arr1 = np.array(A)
    arr2 = np.array(B)
    return (arr1 + arr2).tolist()
    # numpy 객체에서 list로 변환해주어야 함


print(solution([[1, 2], [3, 4]], [[5, 6], [7, 8]]))


def solution2(A, B):
    print([[c+d for c, d in zip(a, b)] for a, b in zip(A, B)])


print(solution2([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
