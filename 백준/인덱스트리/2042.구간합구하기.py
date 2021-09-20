# https://www.acmicpc.net/problem/2042
import sys

read = sys.stdin.readline
n, m, k = map(int, read().split())
# N이 100만
PIV = 1 << 20
leafnode = 1 << 64
tree = [0] * (PIV * 2)


# n은 인덱스, v 는 값
def update(n, v):
    n += PIV
    tree[n] = v
    n //= 2
    while n > 0:
        tree[n] = tree[n * 2] + tree[n * 2 + 1]
        n //= 2


def query(l, r):
    l += PIV
    r += PIV
    ret = 0
    while l <= r:
        # l이 홀수 일때 자기 자신의 값을 더함
        if l % 2 == 1:
            ret += tree[l]
            l += 1
        if r % 2 == 0:
            ret += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return ret


for idx in range(n):
    v = int(read().rstrip())
    update(idx, v)

# print(tree[PIV : PIV + 5])
# print(tree[PIV // 2 : PIV // 2 + 4])
for _ in range(m + k):
    a, b, c = map(int, read().split())
    if a == 1:
        update(b - 1, c)
    elif a == 2:
        print(query(b - 1, c - 1))
