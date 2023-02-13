# 동적계획법
n = int(input())
num= [int(input()) for _ in range(n)]
dp= [0]*(n+1)
dp[1] = num[0]
if n==1 : print(dp[1])
else:
    dp[2] = num[1] +dp[1]
    for i in range(3,n+1):
        dp[i] = max(num[i-1]+dp[i-2],num[i-1]+num[i-2]+dp[i-3],dp[i-1])
    print(max(dp))