from itertools import combinations


def solution(n):
    ans = 0
    sieve = [False, False] + [True] * (n-2)
    # 절반 까지만 검사하면 됨
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i*2, n, i):
                sieve[j] = False
    prime = [i for i in range(2, n) if sieve[i]]
    for val in combinations(prime, 3):
        if sum(val) == n:
            ans += 1
    # print(ans)
    return ans


solution(33)
solution(9)
