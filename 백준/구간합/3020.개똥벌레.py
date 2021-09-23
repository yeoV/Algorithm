# N 은 동굴의 길이(col), H는 동굴의 높이(row)
N, H = map(int, input().split(" "))
top = [0] * (H + 1)
bottom = [0] * (H + 1)
bCheck = True
for _ in range(N):
    val = int(input())
    if bCheck:
        bottom[H - val + 1] += 1
    else:
        top[val] += 1
    bCheck = not bCheck

# 종유석 구간 합
for idx in range(H-1, 0, -1):
    top[idx] = top[idx + 1] + top[idx]
# 석순 구간 합
for idx in range(1, H + 1):
    bottom[idx] = bottom[idx - 1] + bottom[idx]
# top, bottom
# [0, 0, 2, 3, 2, 0]
# [0, 0, 1, 4, 1, 1]
total = [bottom[idx] + top[idx] for idx in range(1, H+1)]
print(min(total), total.count(min(total)))
