import sys
read = sys.stdin.readline
N = int(input())
table = []
for _ in range(N):
    s, e = map(int, read().split())
    table.append((s, e))
# key 값을 순서대로 넣어주면 첫번째 값으로 정렬 후,
# 동일 시 두번쨰 값으로 정렬
table = sorted(table, key=lambda x: (x[1], x[0]))
ans = 0
s, e = 0, 0
for time in table:
    s = time[0]
    if e <= s:
        ans += 1
        e = time[1]
print(ans)
