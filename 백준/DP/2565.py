# https://www.acmicpc.net/problem/2565
import sys
import bisect

read = sys.stdin.readline
n = int(read())
graph = [list(map(int, read().split())) for _ in range(n)]


def run():
    graph.sort(key=lambda x: x[0])
    wires = [node[1] for node in graph]
    dp = []
    for wire in wires:
        idx = bisect.bisect_left(dp, wire)
        if idx == len(dp):
            dp.append(wire)
        else:
            dp[idx] = wire
    return len(wires) - len(dp)


result = run()
print(result)
