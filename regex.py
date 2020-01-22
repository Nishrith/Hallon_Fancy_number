import re
answer = []
string = '982223338'
for i in range(0,10):
    ans = re.findall(str(i) +'{3}',string)
    if ans:
        answer.append(ans)
print(answer)