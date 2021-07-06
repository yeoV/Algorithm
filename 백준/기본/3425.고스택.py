# https://www.acmicpc.net/problem/3425
import sys
read = sys.stdin.readline
cmd = read().strip()
while cmd != 'QUIT':
    command = []
    while cmd != 'END':
        command.append(cmd)
        cmd = read().strip()
    n = int(read().strip())
    for _ in range(n):
        is_error = False
        s = []
        s.append(int(read().strip()))
        try:
            for c in command:
                if c[:3] == 'DUP':
                    s.append(s[-1])
                elif c[:3] == 'NUM':
                    x = c.split()
                    s.append(int(x[1]))
                elif c[:3] == 'POP':
                    s.pop()
                elif c[:3] == 'INV':
                    s[-1] = -s[-1]
                elif c[:3] == 'SWP':
                    s[-1], s[-2] = s[-2], s[-1]
                elif c[:3] == 'ADD':
                    a, b = s.pop(), s.pop()
                    if abs(b + a) > 10 ** 9:
                        is_error = True
                        break
                    s.append(a + b)
                elif c[:3] == 'SUB':
                    a, b = s.pop(), s.pop()
                    if abs(b - a) > 10 ** 9:
                        is_error = True
                        break
                    s.append(b - a)
                elif c[:3] == 'MUL':
                    a, b = s.pop(), s.pop()
                    if abs(a * b) > 10 ** 9:
                        is_error = True
                        break
                    s.append(a * b)
                elif c[:3] == 'DIV':
                    a, b = s.pop(), s.pop()
                    if a == 0:
                        is_error = True
                        break
                    tmp = abs(b) // abs(a)
                    tmp = tmp * -1 if a * b < 0 else tmp
                    s.append(tmp)
                elif c[:3] == 'MOD':
                    a, b = s.pop(), s.pop()
                    if a == 0:
                        is_error = True
                        break
                    tmp = abs(b) % abs(a)
                    tmp = tmp * -1 if b < 0 else tmp
                    s.append(tmp)
        except:
            is_error = True
        if len(s) != 1 or is_error:
            print('ERROR')
        else:
            print(s.pop())
    read().strip()
    print()
    cmd = read().rstrip()
