'''
오름차순으로 정렬된 리스트에서 해당 값의 위치를 찾는 알고리즘
'''
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 33))
