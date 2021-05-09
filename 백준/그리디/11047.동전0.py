import sys
read = sys.stdin.readline
N, K = map(int, read().split())
coins = [int(read().rstrip()) for _ in range(N)]
cnt = 0
coins.sort(reverse=True)
for coin in coins:
    if K == 0:
        break
    if K >= coin:
        while K >= coin:
            K -= coin
            cnt += 1
print(cnt)
