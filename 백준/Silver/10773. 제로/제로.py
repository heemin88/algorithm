# 스택
k = int(input())
result = 0
num=[]
for i in range(k):
    temp = int(input())
    if temp ==0:
        num.pop()
    else:
        num.append(temp)
for i in range(len(num)):
    result += num[i]
print(result)