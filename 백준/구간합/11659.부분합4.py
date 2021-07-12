import sys
read = sys.stdin.readline
N, M = map(int, input().split(" "))
arr = list(map(int, read().rstrip().split(" ")))
prefix = [0] * (len(arr)+1)

for idx in range(1, N+1):
    prefix[idx] = prefix[idx-1] + arr[idx-1]


def prefix_sum(start, end) -> int:
    return prefix[end] - prefix[start - 1]


for _ in range(M):
    x, y = map(int, read().rstrip().split(" "))
    print(prefix_sum(x, y), end='\n')
