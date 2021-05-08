import sys
read = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, read().split()))
arr.sort()
cnt = 0
while arr:
    tape = L - 1
    while arr:
        val = arr[0]
        cnt += 1
        arr.remove(val)
        while arr:
            nxt = arr[0]
            dis = nxt - val
            if tape >= dis:
                arr.remove(nxt)
            else:
                break
print(cnt)
