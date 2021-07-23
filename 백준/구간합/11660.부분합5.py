import sys
read = sys.stdin.readline
N, M = map(int, input().split(" "))
arr = list()
prefix = [[0]*(N+1) for _ in range(N+1)]

for _ in range(N):
    arr.append(list(map(int, read().rstrip().split(" "))))

# 구간합 만들기
for x in range(1, N+1):
    for y in range(1, N+1):
        prefix[x][y] = prefix[x-1][y] + \
            prefix[x][y-1] - prefix[x-1][y-1] + arr[x-1][y-1]
res = list()
for _ in range(M):
    x, y, nx, ny = map(int, input().split(" "))
    res.append(prefix[nx][ny] - prefix[nx][y-1] -
               prefix[x-1][ny] + prefix[x-1][y-1])

for val in res:
    print(val, end="\n")
