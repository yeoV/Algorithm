'''
가장 많이 등장하는 알파벳을 반환
input	output
'aab'	'a'
'dfdefdgf'	'df'
'bbaa'	'ab'
'''
import collections
string = input()
count = collections.Counter(string).most_common()
maxval = 0
answer = ''
for key, val in count:
    if maxval <= val:
        answer += key
        maxval = val
print("".join(sorted(answer)))
