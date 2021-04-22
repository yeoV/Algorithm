import math
numbers = [int(input()) for _ in range(5)]
val = 1
for num in numbers:
    val = val * num
    if math.sqrt(val) == int(math.sqrt(val)):
        print('found')
        break
else:
    print('not found')
