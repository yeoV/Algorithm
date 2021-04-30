N = int(input())
dp_1 = []
dp_2 = []

if N == 1:
    print(1)
else:
    for i in range(N):
        if i == 0:
            dp_1.append(1)
            dp_2.append(0)
        elif i == 1:
            dp_1.append(1)
            dp_2.append(1)
        else:
            dp_1.append(dp_1[i-1] + dp_2[i-1])
            dp_2.append(dp_1[i-2] + dp_2[i-2])
    print((dp_1[-1] + dp_2[-1]) % 10007)
