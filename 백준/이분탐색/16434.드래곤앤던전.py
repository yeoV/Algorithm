# https://www.acmicpc.net/problem/16434
import sys

read = sys.stdin.readline
N, H_ATK = map(int, read().split())
rooms = [tuple(map(int, read().split())) for _ in range(N)]


def do(atk, hp):
    now_hp = hp
    now_atk = atk
    for t, a, h in rooms:
        if t == 1:
        # 몬스터 피 깍기
            mob_cnt = h // now_atk
            mob_cnt += 1 if h % now_atk else 0

            hero_cnt = now_hp // a
            hero_cnt += 1 if now_hp % a else 0

            if mob_cnt > hero_cnt:
                return False
            # 몬스터 먼저 때리는 턴제이기 때문에
            now_hp -= a * (mob_cnt - 1)
        else:
            now_atk += a
            now_hp = now_hp + h if now_hp + h <= hp else hp
    return True


MAX = (10 ** 12) * 123456
s, e = 0, MAX
while s <= e:
    mid = (s + e) // 2
    if do(H_ATK, mid):
        e = mid - 1
    else:
        s = mid + 1
print(s)
