import sys
n,sum = map(int,sys.stdin.readline().split()) #길이 , 합
result =100000001
num=list(map(int,sys.stdin.readline().split()))
right = 0
left =0
r_num=0
while True:
    if r_num>=sum:
        result = min(result,right-left)
        r_num -= num[left]
        left+=1
    elif right ==n:
        break
    else:
        r_num += num[right]
        right +=1
if result == 100000001: print(0)
else: print(result)