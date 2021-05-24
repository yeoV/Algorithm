"""
재귀적으로도 해결해보기
"""


def solution(expression):
    prior = [
        ('-', '+', '*'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('*', '+', '-'),
        ('*', '-', '+'),
        ('-', '*', '+')
    ]
    prev = 0
    ans = 0
    nums, cal = [], []
    for idx, val in enumerate(expression):
        if val == '+' or val == '-' or val == '*':
            nums.append(int(expression[prev:idx]))
            cal.append(val)
            prev = idx+1
    nums.append(int(expression[prev:]))
    # print(nums, cal)
    for pri in prior:
        nums_tmp = nums[:]
        cals_tmp = cal[:]
        for p in pri:
            cal_tmp = []
            cal_order = 0
            for i in range(len(cals_tmp)):
                if cals_tmp[i] == p:
                    cal_tmp.append(i)
            for c_idx in cal_tmp:
                c_idx -= cal_order
                if p == '-':
                    nums_tmp.insert(c_idx, nums_tmp.pop(
                        c_idx) - nums_tmp.pop(c_idx))
                    cals_tmp.pop(c_idx)

                elif p == '+':
                    nums_tmp.insert(c_idx, nums_tmp.pop(
                        c_idx) + nums_tmp.pop(c_idx))
                    cals_tmp.pop(c_idx)
                else:
                    nums_tmp.insert(c_idx, nums_tmp.pop(
                        c_idx) * nums_tmp.pop(c_idx))
                    cals_tmp.pop(c_idx)
                cal_order += 1
        ans = max(ans, abs(nums_tmp[0]))
    # print(ans)
    return ans


solution("100-200*300-500+20")
