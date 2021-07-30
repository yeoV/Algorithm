# https://www.acmicpc.net/problem/1039
import sys
from collections import deque
from itertools import combinations
read = sys.stdin.readline
n, k = read().split()
k = int(k)


def bfs(n):
    ret = -1
    q = deque([n])
    for epo in range(k):
        # print(f'epoch : {epo}, q len : {len(q)}')
        for i in range(len(q)):
            nums = list(q.popleft())

            for a, b in combinations(range(len(n)), 2):
                tmp = nums[:]
                tmp[a], tmp[b] = tmp[b], tmp[a]
                tmp = "".join(tmp)
                if tmp[0] == '0':
                    continue
                if epo == k-1:
                    ret = max(ret, int(tmp))
                q.append(tmp)
        q = deque(list(set(q)))

    return ret


print(bfs(n))
