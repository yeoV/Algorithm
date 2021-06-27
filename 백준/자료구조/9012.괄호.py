import sys
read = sys.stdin.readline
T = int(read().rstrip())


ans = []
for _ in range(T):
    stack = []
    pstr = read().rstrip()
    for val in pstr:
        if val == ')':
            if stack:
                stack.pop()
            else:
                ans.append('NO')
                break
        else:
            stack.append(val)

    else:
        if stack:
            ans.append('NO')
        else:
            ans.append('YES')
print(*ans, sep='\n')
