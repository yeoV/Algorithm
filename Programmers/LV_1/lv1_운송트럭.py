def solution(max_weight, specs, names):
    specs = dict(specs)
    cnt = 1
    weight = 0
    for name in names:
        weight += int(specs[name])
        if max_weight < weight:
            cnt += 1
            weight = int(specs[name])
            print(name)
    print(cnt)


solution(300, [["toy", "70"], ["snack", "200"]], ["toy", "snack", "snack"])
solution(200, [["toy", "70"], ["snack", "200"]], ["toy", "snack", "toy"])
