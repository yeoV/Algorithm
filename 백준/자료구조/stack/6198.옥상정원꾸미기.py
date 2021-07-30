# https://www.acmicpc.net/problem/6198
import sys
read = sys.stdin.readline
n = int(read().rstrip())
building = [int(read().rstrip()) for _ in range(n)]

stack = []
ans = 0
print(building)
for idx, val in enumerate(building):
    print(stack)
    while stack and stack[-1] <= val:
        stack.pop()
    stack.append(val)
    ans += len(stack) - 1
print(ans)
