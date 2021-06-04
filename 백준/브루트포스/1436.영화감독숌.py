# https://www.acmicpc.net/problem/1436
n = int(input())
number = 0
while n:
    if '666' in str(number):
        n -= 1
    number += 1
print(number-1)
