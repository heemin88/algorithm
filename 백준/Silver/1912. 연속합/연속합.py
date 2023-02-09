# 동적계획법
n = int(input())
num =[0]*n
num = list(map(int,input().split()))
max = max(num)
dp = [0]*n
dp[0] = num[0]
for i in range(1,n):
    if dp[i-1] <0:dp[i] = num[i]
    elif dp[i-1]+num[i] <0 :
        dp[i]= -1
    else:
        dp[i] = dp[i-1]+num[i]
    if dp[i]>max:
        max = dp[i]

print(max)