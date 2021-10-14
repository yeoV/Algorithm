# https://www.acmicpc.net/problem/10090
import sys

read = sys.stdin.readline
n = int(read().rstrip())
PIV = 1 << 20
tree = [0] * (PIV * 2)
arr = [(v, i) for i, v in enumerate(map(int, read().split()))]
# arr = sorted(arr, key=lambda x: (-x[0], -x[1]))
arr = sorted(arr, key=lambda x: (-x[0]))


def update(n):
    n += PIV
    tree[n] += 1
    n //= 2
    while n > 0:
        tree[n] = tree[n * 2] + tree[n * 2 + 1]
        n //= 2


def query(left, right):
    left += PIV
    right += PIV
    ret = 0
    while left <= right:
        if left % 2 == 1:
            ret += tree[left]
            left += 1
        if right % 2 == 0:
            ret += tree[right]
            right -= 1
        left //= 2
        right //= 2

    return ret


ans = 0
for val in arr:
    ans += query(0, val[1] - 1)
    update(val[1])
print(ans)
