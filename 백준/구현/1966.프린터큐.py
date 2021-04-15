from collections import deque
import sys
read = sys.stdin.readline

T = int(read().rstrip())
for _ in range(T):
    N, target = map(int, read().rstrip().split())
    # 내가 궁금한 문서
    target_arr = [False] * N
    target_arr[target] = True

    docs_arr = [i for i in range(N)]
    priority = list(map(int, read().rstrip().split()))
    q = deque(list(zip(docs_arr, priority, target_arr)))

    priority = sorted(priority, reverse=True)
    max_val_idx = 0
    cnt = 1

    while q:
        max_val = priority[max_val_idx]
        docs, pri, istarget = q.popleft()
        print(q)
        # 타겟일 경우
        if pri == max_val:
            if istarget:
                print(cnt)
                break
            else:
                cnt += 1
                max_val_idx += 1
                continue
        else:
            q.append((docs, pri, istarget))
