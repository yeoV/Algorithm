import sys
read = sys.stdin.readline
N, K = map(int, read().split())
arr = list(map(int, read().split()))
cnt = [0] * 100001
start = 0
res = 0

for end in range(N):
    cnt[arr[end]] += 1
    if cnt[arr[end]] > K:
        res = max(res, end - start)
        while cnt[arr[end]] > K:
            cnt[arr[start]] -= 1
            start += 1
res = max(res, end - start + 1)
print(res)
