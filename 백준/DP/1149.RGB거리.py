import sys
read = sys.stdin.readline
N = int(input())
RGB = [list(map(int, read().split())) for _ in range(N)]
R, G, B = zip(*RGB)
dp_r, dp_g, dp_b = [], [], []
for i in range(N):
    # 초기값 세팅
    if i == 0:
        dp_r.append(R[0])
        dp_g.append(G[0])
        dp_b.append(B[0])
    else:
        dp_r.append(min(dp_g[i-1] + R[i], dp_b[i-1] + R[i]))
        dp_g.append(min(dp_r[i-1] + G[i], dp_b[i-1] + G[i]))
        dp_b.append(min(dp_r[i-1] + B[i], dp_g[i-1] + B[i]))
print(min(dp_r[-1], dp_g[-1], dp_b[-1]))
