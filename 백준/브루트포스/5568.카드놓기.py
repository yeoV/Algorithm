# https://www.acmicpc.net/problem/5568
import sys
from itertools import permutations

read = sys.stdin.readline

n = int(read().rstrip())
k = int(read().rstrip())
cards = [read().rstrip() for _ in range(n)]

ans_set = set()
for comb in permutations(cards, k):
    ans_set.add(int("".join(comb)))
print(len(ans_set))
