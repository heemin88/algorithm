# 동적계획법
n = int(input())
num =[0]*n
dp = [0]*n
for i in range(n):
    num[i] = int(input())
if len(num)<=2:
    print(sum(num))
else:
    dp[0] = num[0]
    dp[1] = num[0]+num[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+num[i-1]+num[i],dp[i-2]+num[i])
    print(dp[n-1])
