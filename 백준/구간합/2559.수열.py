import sys
read = sys.stdin.readline
N, K = map(int, read().rstrip().split(" "))
arr = list(map(int, read().rstrip().split(" ")))
prefix = [0] * (N + 1)
for idx in range(1, N+1):
    prefix[idx] = prefix[idx - 1] + arr[idx-1]


def prefix_sum(start, end) -> int():
    # print(prefix[end] - prefix[start - 1])
    return prefix[end] - prefix[start - 1]


res = -float('inf')         # 답이 음수인 경우 생각하기
for start in range(1, len(prefix)):
    end = start + K-1
    if end > len(prefix) - 1:
        break
    res = max(res, prefix_sum(start, end))
print(res)
