n = int(input())
tpah = []
dp = [[] for _ in range(n)]
for i in range(n):
    tpah.append(list(map(int,input().split())))

dp[0]=tpah[0]

for i in range(1,n):
    for j in range(len(tpah[i])):
       if j ==0 : dp[i].append(dp[i-1][j]+ tpah[i][j])
       elif j == len(tpah[i])-1 : dp[i].append(dp[i-1][j-1]+ tpah[i][j])
       else:
           dp[i].append(max(dp[i-1][j-1],dp[i-1][j]) + tpah[i][j])
print(max(dp[n-1]))