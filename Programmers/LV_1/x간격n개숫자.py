def solution(x, n):
    return [x + x*i for i in range(n)]


print(solution(3, 6))
print(solution(-4, 3))
