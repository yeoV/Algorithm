# https://www.acmicpc.net/problem/14888
from itertools import permutations
import sys

read = sys.stdin.readline
n = int(read().rstrip())
numbers = list(map(int, read().split()))
# + - * %
operator = ['+', '-', '*', '//']
calc = []
ans = [-float('inf'), float('inf')]
for idx, val in enumerate(map(int, read().split())):
    calc.extend([operator[idx]] * val)\

print(calc)

for per in permutations(calc, len(calc)):
    tmp = numbers[0]
    for idx in range(n-1):
        if per[idx] == '+':
            tmp += numbers[idx + 1]
        elif per[idx] == '-':
            tmp -= numbers[idx + 1]
        elif per[idx] == '*':
            tmp *= numbers[idx + 1]
        else:
            if tmp < 0:
                tmp = -int(abs(tmp) // numbers[idx + 1])
            else:
                tmp = int(tmp // numbers[idx + 1])

    ans[0] = max(ans[0], tmp)
    ans[1] = min(ans[1], tmp)

print(*map(int, ans), sep='\n')
