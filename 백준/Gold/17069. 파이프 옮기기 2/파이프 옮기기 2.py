n = int(input())
home =[]
result =0
dp=[[[0]*3 for _ in range(n)]for _ in range(n)]
# 0 : 가로 , 1: 세로, 2 : 대각선
for i in range(n): # 0,0 -> n,n
    home.append(list(map(int,input().split())))
dp[0][1][0] = 1
for i in range(n):
    if home[0][i]==1:
        break
    dp[0][i][0] =1
for i in range(1,n):
    for j in range(2,n):
        if not home[i][j]: #가로
            dp[i][j][0] = dp[i][j-1][0]+dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1]+dp[i-1][j][2]
        if not home[i][j] and not home[i-1][j] and not home[i][j-1]:
            dp[i][j][2] = dp[i-1][j-1][0]+dp[i-1][j-1][2] +dp[i-1][j-1][1]
print(sum(dp[-1][-1]))