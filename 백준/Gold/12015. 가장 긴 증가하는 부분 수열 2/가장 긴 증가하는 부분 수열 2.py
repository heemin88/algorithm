n = int(input())
a = list(map(int,input().split()))
result =1
dp=[]
def check(num):
    start =0
    end = len(dp)-1
    while start <=end:
        mid = (start+end)//2
        if num > dp[mid]:
            start= mid+ 1
        else:
            end = mid-1
    return start
for num in a:
    if not dp: #비어있으면
        dp.append(num)
    else:
        pos = check(num)
        if pos>=len(dp):
            dp.append(num)
        else:
            dp[pos] =num
print(len(dp))
