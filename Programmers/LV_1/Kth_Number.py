def solution(array, commands):
    answer = []
    for element in commands:
        tmp = array
        i, j, k = element
        answer.append(sorted(tmp[i - 1 : j])[k - 1])
    return answer


# Using List Comprehension
def solution2(array, commands):
    return [
        sorted(array[i - 1 : j])[k - 1] for i, j, k in [element for element in commands]
    ]



#Using map func
def solution3(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
