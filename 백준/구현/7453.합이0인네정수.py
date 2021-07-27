# https://www.acmicpc.net/problem/7453
import sys
from collections import Counter
read = sys.stdin.readline
A, B, C, D = [], [], [], []
n = int(read().rstrip())
for _ in range(n):
    a, b, c, d = map(int, read().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
# CD = defaultdict(int)
CD = []
# O(N^2)
for c in C:
    for d in D:
        CD.append(c+d)
CD = Counter(CD)
cnt = 0
for a in A:
    for b in B:
        cnt += CD[-(a+b)]
print(cnt)
