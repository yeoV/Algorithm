import sys
from collections import Counter
read = sys.stdin.readline
N = int(input())
arr = list(map(int, read().split()))
count_arr = Counter(arr)
tmp = 1e9
two_cnt = 0
one_cnt = 0
# 1. 최대값의 range가 모두 포함되지 않은 경우
max_val = set(range(max(arr) + 1))
for val in max_val:
    if val not in arr:
        print(0)
        exit()
# 2. 유효성 검사
for key in sorted(count_arr.keys()):
    # 갯수가 2개 초과인 경우
    if count_arr[key] > 2:
        print(0)
        exit()
    # 이전의 값보다 다음의 값이 더 큰 경우
    if tmp < count_arr[key]:
        print(0)
        exit()
    # 값이 2이거나 1 인 경우
    if count_arr[key] == 2:
        two_cnt += 1
    if count_arr[key] == 1:
        one_cnt = 1
    tmp = count_arr[key]
print(2**(two_cnt + one_cnt))
