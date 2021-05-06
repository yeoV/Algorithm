import sys
read = sys.stdin.readline
s = read().rstrip()
ans0, ans1 = 0, 0  # 전부 0과 1로 바꾸는 경우

# if s[0] == '1':
#     ans0 += 1
# else:
#     ans1 += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            ans0 += 1
        else:
            ans1 += 1
print(ans1, ans0)
print(min(ans1, ans0))
