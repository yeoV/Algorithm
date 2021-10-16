# https://programmers.co.kr/learn/courses/30/lessons/81303
"""
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
"""
from collections import defaultdict


def solution(n, k, cmd):
    table = defaultdict(list)
    erase_stack = []
    table[0] = [n-1, 1]
    for idx in range(1, n-1):
        table[idx] = [idx - 1, idx + 1]
    table[n-1] = [n-2, 0]
    print(table)

    cur = k
    for c in cmd:
        print(cur, table)
        c = c.split()
        if c[0] == 'D':
            for _ in range(int(c[1])):
                cur = table[cur][1]
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                cur = table[cur][0]
        elif c[0] == 'C':
            erase_stack.append((cur, table[cur]))
            table[table[cur][0]][1] = table[cur][1]
            table[table[cur][1]][0] = table[cur][0]
            tmp = table[cur]
            del table[cur]
            if tmp[1] == 0: # 맨 마지막 노드
                cur = tmp[0]
            else:
                cur = tmp[1]

        elif c[0] == 'Z':
            node, val = erase_stack.pop()
            table[node] = val
            table[val[0]][1] = node
            table[val[1]][0] = node
    ans = ""
    for idx in range(n):
        if table.get(idx):
            ans += 'O'
        else:
            ans += 'X'
    print(ans)

solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"])
# solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
# solution(5, 2, ['D 2'])
