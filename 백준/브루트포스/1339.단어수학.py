import sys
from collections import defaultdict
read = sys.stdin.readline
n = int(read().rstrip())
arrays = [read().rstrip() for _ in range(n)]
score = defaultdict(int)

for arr in arrays:
    for idx, val in enumerate(arr):
        score[val] += 10 ** (len(arr) - idx - 1)


res = 0
num = 9
# 가장 큰 값부터 내림차순 정렬
for val in sorted(score.items(), key=lambda x: -x[1]):
    res += num * val[1]
    num -= 1

print(res)
