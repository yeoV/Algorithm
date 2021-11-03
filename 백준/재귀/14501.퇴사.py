import sys

sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

n = int(read().rstrip())
arr = []
for _ in range(n):
    a, b = map(int, read().split())
    arr.append((a, b))

ans = 0


def run(prev_day, cost):
    global ans
    ans = max(ans, cost)

    if prev_day >= n:
        return

    now_day, now_cost = arr[prev_day]
    if now_day + prev_day <= n:
        run(now_day + prev_day, cost + now_cost)

    if prev_day + 1 <= n:
        run(prev_day + 1, cost)
    return


run(0, 0)
print(ans)
