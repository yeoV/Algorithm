'''
최대 공약수와 공배수 리스트로 리턴
유클리드 호제법 이용
'''


def solution(n, m):
    def gcd(a, b): return a if b == 0 else gcd(b, a % b)
    # def gcd(a,b): return b if not a%b else gdc(b, a%b)
    def lcm(a, b): return (n*m) // gcd(a, b)
    return [gcd(n, m), lcm(n, m)]


print(solution(4, 12))
