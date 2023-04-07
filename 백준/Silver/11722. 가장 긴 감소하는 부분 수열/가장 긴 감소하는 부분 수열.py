n = int(input())
a = list(map(int,input().split()))
dp=[0 for _ in range(n)]
dp[0]= 1
result =dp[0]
for i in range(n):
    tmp = 0
    for j in range(i-1,-1,-1):
        if a[i]< a[j]:
            tmp = max(tmp,dp[j])
    dp[i]= tmp +1
    result = max(result,dp[i])
print(result)