"""
입력받은 좌표에서 나이트가 이동할 수 있는 좌표의 갯수반환
a1
결과 2
c2
결과 6
"""


def solution():
    spot = input()
    col = spot[0]
    row = int(spot[1])
    col = int(ord(col) - ord('a') + 1)
    count = 0
    print(col, row)
    steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2),
             (2, 1), (2, -1), (1, -2), (-1, 2)]

    for step in steps:
        row_next = row + step[0]
        col_next = col + step[1]
        if row_next < 1 or col_next < 1:
            continue
        count += 1
    return count


if __name__ == "__main__":
    print(solution())
