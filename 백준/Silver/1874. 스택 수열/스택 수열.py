# 스택
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
result = []
sort_num = sorted(num)
temp = []
j = 0 # num index
i=0 # sort_num index
while i <n:
    temp.append(sort_num[i])
    result.append('+')
    k = len(temp) - 1 #temp index
    while temp[k] == num[j]:
        temp.pop()
        result.append('-')
        j += 1
        k -= 1
        if j >=n or k<0: break
    i += 1
if len(temp)!= 0:
    print("NO")
else:
    for i in result:
        print(i)