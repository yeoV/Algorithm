import sys
read = sys.stdin.readline
N = int(input())
p = list(map(int, read().split()))
p.sort()
ans, i = 0, N
for t in p:
    ans += t * i
    i -= 1
print(ans)
