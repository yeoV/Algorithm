def solution(record):
    id_dict = dict()
    log = list()
    answer = list()
    for rec in record:
        rec = rec.split(" ")
        if len(rec) == 2:  # Leave
            action, uid = rec[0], rec[1]
            log.append([uid, '님이 나갔습니다.'])
        else:
            action, uid, name = rec[0], rec[1], rec[2]
            if action == 'Enter':
                id_dict[uid] = name
                log.append([uid, '님이 들어왔습니다.'])
            elif action == 'Change':
                if uid in id_dict:
                    id_dict[uid] = name
    for ans in log:
        ans[0] = id_dict[ans[0]]
        answer.append("".join(ans))
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
