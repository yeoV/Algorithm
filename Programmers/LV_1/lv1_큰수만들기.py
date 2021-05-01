# 1. 큰수를 우선하여 담기
# 2. 일단 담고 큰수가 나오면 뺴기
# 주어진 숫자로 하나씩 꺼내되, 모아둔 것 중 지금보다 작은것들 k개 만큼 뺌
def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer
