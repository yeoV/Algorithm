# https://www.acmicpc.net/problem/4659
import sys
import re

read = sys.stdin.readline

"""
1. 모음 반드시 하나 포함
2. 모음 3개 혹은 자음 3개 연속 x
3. 같은 글자 연속 2번 x 
"""
while True:
    pwd = read().rstrip()
    if pwd == "end":
        exit()
    if not re.findall("[aeiou]", pwd):
        print("<" + pwd + ">" + " is not acceptable.")

    elif re.findall("[aieou]{3}", pwd) or re.findall("[^aeiou]{3}", pwd):
        print("<" + pwd + ">" + " is not acceptable.")

    elif re.findall(r"(([a-z])\2+)", pwd) and not re.findall(r"(([eo])\2+)", pwd):
        print("<" + pwd + ">" + " is not acceptable.")
    else:
        print("<" + pwd + ">" + " is acceptable.")
