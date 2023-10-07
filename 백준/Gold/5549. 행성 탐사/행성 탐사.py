import sys
input = sys.stdin.readline
m,n = map(int,input().split())
k = int(input())
map_content = []
for i in range(m):
    map_content.append(list(input()))
search =[]
for i in range(k):
    search.append(list(map(int,input().split())))
#각 조사 대상 영역에 포함되어 있는 정글, 바다, 얼음의 수를 공백으로 구분해 한 줄에 한 정보씩 출력
dp = [[[0,0,0] for _ in range(n+1)] for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        dp[i][j][0] = dp[i - 1][j][0] + dp[i][j - 1][0] - dp[i - 1][j - 1][0]
        dp[i][j][1] = dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1]
        dp[i][j][2] = dp[i - 1][j][2] + dp[i][j - 1][2] - dp[i - 1][j - 1][2]
        if map_content[i-1][j-1] == 'J':
            dp[i][j][0] +=1
        elif map_content[i-1][j-1] =='O':
            dp[i][j][1] +=1
        else:
            dp[i][j][2] += 1
for s in search:
    a,b,c,d = s[0],s[1],s[2],s[3]
    print(dp[c][d][0] - dp[c][b-1][0]-dp[a-1][d][0] + dp[a-1][b-1][0],dp[c][d][1] - dp[c][b-1][1]-dp[a-1][d][1] + dp[a-1][b-1][1],dp[c][d][2] - dp[c][b-1][2]-dp[a-1][d][2] + dp[a-1][b-1][2])
