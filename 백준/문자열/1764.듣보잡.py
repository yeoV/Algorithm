import sys

read = sys.stdin.readline

N, M = map(int, read().split())

not_listen = {read().rstrip() for _ in range(N)}
not_look = {read().rstrip() for _ in range(M)}

res = sorted(not_listen & not_look)
print(len(res))
for val in res:
    print(val)
