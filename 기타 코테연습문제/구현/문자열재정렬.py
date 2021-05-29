s = input()
number, string = 0, []
for i in s:
    if i.isdigit():
        number += int(i)
    else:
        string.append(i)
# 만약 숫자가 0인경우
string.sort()
if number > 0:
    string.append(str(number))
print("".join(string))
