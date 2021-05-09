import sys
read = sys.stdin.readline
info = []
while True:
    L, P, V = map(int, read().split())
    if (V, P, V) == (0, 0, 0):
        break
    info.append((L, P, V))

days = []
for val in info:
    day = 0
    L, P, V = val
    if V//P:
        day += L * (V//P)

    mod = V % P
    if mod >= L:
        day += L
    else:
        day += mod
    days.append(day)
for i in range(1, len(days)+1):
    print(f'Case {i}: {days[i-1]}')
