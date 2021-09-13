def time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    tmp = h * 3600 + m * 60 + s
    return tmp


def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    # 맨 마지막 인덱스
    time_line = [0] * (play_sec + 1)
    for log in logs:
        log = log.split("-")
        start, end = time_to_sec(log[0]), time_to_sec(log[1])
        time_line[start] += 1
        time_line[end] -= 1

    for i in range(1, len(time_line)):
        time_line[i] += time_line[i - 1]
    current_sum = sum(time_line[:adv_sec])
    # 맨 처음 값
    ans = [current_sum, 0]
    for j in range(adv_sec, play_sec):
        current_sum = current_sum + time_line[j] - time_line[j - adv_sec]
        if ans[0] < current_sum:
            ans[0] = current_sum
            ans[1] = j - adv_sec + 1
    ans = f"{int(ans[1] / 3600):02d}:{int(ans[1]/60%60):02d}:{int(ans[1]%60):02d}"
    print(ans)
    return ans


# solution(
#     "02:03:55",
#     "00:14:15",
#     [
#         "01:20:15-01:45:14",
#         "00:40:31-01:00:00",
#         "00:25:50-00:48:29",
#         "01:30:59-01:53:29",
#         "01:37:44-02:02:30",
#     ],
# )

solution(
    "99:59:59",
    "25:00:00",
    [
        "69:59:59-89:59:59",
        "01:00:00-21:00:00",
        "79:59:59-99:59:59",
        "11:00:00-31:00:00",
    ],
)
