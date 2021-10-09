# https://www.acmicpc.net/problem/10173
import sys

read = sys.stdin.readline
while 1:
    s = read().rstrip()
    if s == "EOI":
        break
    print("Found" if "nemo" in s.lower() else "Missing")
