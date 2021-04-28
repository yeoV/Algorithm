# 4 6
# 19 15 10 17
# 결과 15
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
end = max(arr) - 1
start, result = 0, 0
while start <= end:
    mid = (start + end) // 2
    for val in arr:
        if mid > val:   # mid 값이 떡의 길이보다 긴 경우
            result += val - mid
    if result == M:
        print(mid)
        break
    elif result > M:
        start = mid - 1
    else:
        end = mid + 1

    result = 0
