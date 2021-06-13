import sys
read = sys.stdin.readline
N = int(input())
arr = [int(read().rstrip()) for _ in range(N)]
# N이 1인 경우
if N == 1:
    print(arr[-1])
else:

    dp_1 = [arr[0], arr[1]]
    dp_2 = [0, arr[0]+arr[1]]

    for i in range(2, N):
        dp_1.append(max(dp_1[i-2] + arr[i], dp_2[i-2] + arr[i]))
        dp_2.append(max(0, dp_1[i-1] + arr[i]))
    print(max(dp_1[-1], dp_2[-1]))
    print(dp_1, dp_2)
