# 그리디 알고리즘
cer = list(input())
str = ""
num =0
nums =[]
cnt =0

for i in range(len(cer)):
    if cer[i] == '-':
        if num !=0:
            nums.append(num+int(str))
            num=0
        else :
            nums.append(int(str))
        str=""
        cnt+=1

    elif cer[i] =='+':
        num += int(str)
        str=""
    else:
        str += cer[i]
nums.append(num+int(str))
result = nums[0]

for i in range(cnt):
    result -= nums[i+1]
print(result)