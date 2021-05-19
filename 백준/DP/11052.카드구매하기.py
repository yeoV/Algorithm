import sys
read = sys.stdin.readline
N = int(input())
cards = [0]
cards.extend(list(map(int, read().split())))
dp = [0] * (N+1)

for i in range(1, N+1):  # dp의 인덱스 지정
    for card in range(1, N+1):
        if i - card >= 0:
            # val = max(cards[i], dp[i - card] + cards[card])
            # dp[i] = max(dp[i],val)
            dp[i] = max(dp[i], max(cards[i], dp[i - card] + cards[card]))
print(dp[-1])
