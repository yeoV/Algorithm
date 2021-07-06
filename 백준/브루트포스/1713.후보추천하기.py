# https://www.acmicpc.net/problem/1713
import sys
read = sys.stdin.readline
n = int(read().rstrip())
r = int(read().rstrip())
recommand = list(map(int, read().split()))
frame = dict()

time = 0
for rec in recommand:
    # 이미 있는 사진일 경우
    if rec in frame.keys():
        frame[rec][0] += 1
        # time += 1 <- 오류가 났던 이유 : 단순히 추천만 늘려주는데 time을 늘려줄 필요가 없음
    else:
        # 게시된 사진이 n보다 작을 경우
        if time < n:
            frame[rec] = [1, time]
            time += 1
        # 제거해야 하는 경우
        else:
            # 추천수를 기준으로 정렬, 추천이 동일할 경우 시간순으로 정렬됨
            idx = sorted(frame.items(), key=lambda x: x[1])[0][0]
            frame.pop(idx)
            frame[rec] = [1, time]
            time += 1
for idx in sorted(frame.keys()):
    print(idx, end=' ')
