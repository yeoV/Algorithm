# https://www.acmicpc.net/problem/1072
import sys
read = sys.stdin.readline
x, y = map(int, read().split())
z = int((y * 100) / x)

if z == 100 or z == 99:
    print(-1)
    exit()
s, e = 1,  1000000000

while s <= e:
    mid = (s+e) // 2
    nx = x + mid
    ny = y + mid
    nz = int((ny*100) / nx)

    # 승률이 변했을 경우
    if z < nz:
        e = mid - 1
    else:
        s = mid + 1

print(e+1)
