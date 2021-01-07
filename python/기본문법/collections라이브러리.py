'''
deque는 데이터를 왼쪽에서 삽입하고 뺄 경우 리스트보다 빠르다.
'''

from collections import deque, Counter
data = deque([2, 3, 4])
data.append(10)
data.appendleft(1)
print(data)
print(list(data))


'''
Counter는 data의 갯 수를 세서 구하는 모듈
'''
counter = Counter(['A', 'B', 'C', 'D', 'A', 'C'])
print(counter['A'])
print(counter.most_common())
print(dict(counter))
