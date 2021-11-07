# https://programmers.co.kr/learn/courses/30/lessons/17676


def solution(lines):
    time_line = []
    for line in lines:
        line = line.split(" ")
        tmp = line[1].split(":")
        time = int(tmp[0]) * 3600 + int(tmp[1]) * 60 + float(tmp[2])
        time_line.append((time - float(line[2][:-1]) + 0.001, time))
        # time_line.append(time)
    # print(time_line)

    ans = 0
    for idx in range(len(time_line)):
        cnt = 0
        for val in time_line[idx:]:
            if time_line[idx][1] + 1 > val[0]:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
    return ans


solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
solution(
    [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s",
    ]
)
