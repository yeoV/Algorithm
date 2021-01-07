import itertools

'''
itertools.permutations -> 모든 순열 구하기
'''
data = ['A', 'B', 'C']
print(list(itertools.permutations(data, 2)))


'''
itertools.combinations -> 모든 조합 구하기
'''
print(list(itertools.combinations(data, 2)))

'''
itertools.product -> 모든 곱 구하기
'''
print(list(itertools.product(data, repeat=2)))

'''
itertools.combinations_with_replacement -> 중복을 허용하는 조합
'''
print(list(itertools.combinations_with_replacement(data, 2)))

"""
실행 결과 
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
[('A', 'B'), ('A', 'C'), ('B', 'C')]
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
"""