n, m = map(int, input().split())

# 유클리드 호제법 이용


def GCD(n, m):
    mod = 1
    while mod > 0:
        mod = n % m
        n = m
        m = mod
    return n


gcd = GCD(n, m)
print(gcd)
print(int(m*n/gcd))
