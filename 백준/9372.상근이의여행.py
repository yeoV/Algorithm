import sys
read = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, read().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, read().split())
    print(N-1)
