# 5
# 8 3 7 9 2
# 3
# 5 7 9
import sys
N = int(input())    # 가게에 가지고 있는 물건 갯수
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# set 으로도 구현 가능
arr = set(map(int, input().split(" ")))
M = int(input())    # 손님이 찾으려는 물건 갯수
find_arr = list(map(int, input().split(" ")))
for find in find_arr:
    if find in arr:
        print("yes", end=" ")
    else:
        print("no", end=" ")
