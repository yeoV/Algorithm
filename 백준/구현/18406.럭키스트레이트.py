import sys
read = sys.stdin.readline
N = read().rstrip()
left, right = map(int, N[:(len(N)//2)]), map(int, N[(len(N)//2):])
if sum(left) == sum(right):
    print("LUCKY")
else:
    print('READY')
