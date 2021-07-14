# https://www.acmicpc.net/problem/2606
from collections import defaultdict
import sys
read = sys.stdin.readline
total_pc = int(input())
pair_pc = int(input())
pc_info = defaultdict(set)
for _ in range(pair_pc):
    key, val = map(int, read().split(" "))
    pc_info[key].add(val)
    pc_info[val].add(key)


def dfs(pc_info, val):
    if pc_info[val]:
        for nxt in pc_info[val]:
            if nxt not in visited:
                visited.append(nxt)
                dfs(pc_info, nxt)
    else:
        return


visited = []
# print(pc_info)
dfs(pc_info, 1)
print(len(visited) - 1)
