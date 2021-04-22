def solution2():
    n, m = map(int, input().split())
    for _ in range(m):
        for _ in range(n):
            print('*', end='')
        print()


def solution():
    n, m = map(int, input().split())
    answer = ('*' * n + '\n') * m
    print(answer)


if __name__ == "__main__":
    solution()
