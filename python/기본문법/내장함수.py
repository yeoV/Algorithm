'''
eval 함수는 수학 수식이 문자열 형식으로 들어올 경우 해당 수식을 계산환 결과를 반환
'''
result = eval('(3+5)*7')
print(result)

'''
sorted 함수는 iterable 객체를 정렬한 결과를 list로 반환
'''
result = [9, 5, 3, 1, 2]
print(sorted(result))
print(sorted(result, reverse=True))

# 원하는 key 값으로 정렬 가능
print(sorted([('a', 25), ('b', 75), ('c', 50)], key=lambda x: x[1]))

data = [9, 5, 3, 1, 2]
data.sort()  # sort는 객체 내부값을 변경함
print(data)
