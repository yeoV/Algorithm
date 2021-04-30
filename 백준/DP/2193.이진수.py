N = int(input())

if N > 1:
    dp_0 = [0] * N
    dp_1 = [0] * N
    dp_1[0] = 1
    dp_1[1] = 0
    dp_0[1] = 1
    for i in range(2, N):
        dp_1[i] = dp_0[i-1]
        dp_0[i] = dp_0[i-1] + dp_1[i-1]
    print(dp_1[-1] + dp_0[-1])
else:
    print(1)
