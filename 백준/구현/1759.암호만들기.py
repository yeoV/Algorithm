# https://www.acmicpc.net/problem/1759

"""
* combinattion을 이용하여 풀기
"""

from itertools import combinations
import sys
read = sys.stdin.readline
L, C = map(int, read().split())
alpha = sorted(read().split())
vowel = {'a', 'e', 'i', 'o', 'u'}

for comb in combinations(alpha, L):
    if 0 < len(set(comb) & vowel) <= L-2:
        print("".join(comb))


"""
* 다른 방식으로 풀기, dfs로 해결하기
"""
L, C = map(int, read().split())
alpha = sorted(read().split())
vowel = {'a', 'e', 'i', 'o', 'u'}


def combination(d, prev, arr):
    if d == L:
        if 0 < len(set(arr) & vowel) <= L-2:
            print("".join(arr))
            return
        else:
            return

    for i in range(prev, len(alpha)):
        combination(d+1, i+1, arr + alpha[i])


combination(0, 0, "")
