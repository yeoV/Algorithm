from math import factorial
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial(M) // (factorial(N) * factorial(M-N)))


# def comb(lst, n):
#     ret = []
#     if n > len(lst):
#         return ret

#     if n == 1:
#         for i in lst:
#             ret.append([i])
#     elif n > 1:
#         for i in range(len(lst)-n+1):
#             for temp in comb(lst[i+1:], n-1):
#                 ret.append([lst[i]]+temp)

#     return ret


# print(comb([1, 2, 3, 4], 3))
