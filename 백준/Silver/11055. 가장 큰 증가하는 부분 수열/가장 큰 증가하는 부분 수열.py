n = int(input())
a = list(map(int,input().split()))
dp=[0 for _ in range(n)]
dp[0]= a[0]
result = dp[0]
for i in range(1,n):
    tmp =0
    for j in range(i-1,-1,-1):
        if a[j] < a[i]:
            tmp = max(tmp,dp[j])
    dp[i] = tmp+a[i]
    result = max(result,dp[i])
#print(dp)
print(result)