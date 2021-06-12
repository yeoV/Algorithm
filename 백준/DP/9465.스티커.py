import sys
read = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(read().rstrip())
    arr = [list(map(int, read().split())) for _ in range(2)]
    # 위와 아래가 교차하며 진행
    dp_up, dp_down = [], []
    for i in range(N):
        if i == 0:
            dp_up.append(arr[0][i])
            dp_down.append(arr[1][i])
        elif i == 1:
            dp_up.append(dp_down[0] + arr[0][i])
            dp_down.append(dp_up[0] + arr[1][i])
        else:
            dp_up.append(max(dp_down[i-1] + arr[0][i],
                             dp_down[i-2] + arr[0][i]))
            dp_down.append(max(dp_up[i-1] + arr[1][i], dp_up[i-2] + arr[1][i]))
    print(max(dp_up[-1], dp_down[-1]))
