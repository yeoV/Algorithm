"""길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다."""


def solution(n):
    print("".join(["수" if i % 2 == 0 else "박" for i in range(0, n)]))


solution(3)
solution(5)


def solution2(n):
    print("".join(["수박"[i % 2] for i in range(n)]))


solution2(5)
solution2(3)
