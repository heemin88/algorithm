t = int(input())
MAX = float('INF')
for k in range(t):
    n = int(input())  # 스티커 갯수
    score = [list(map(int, input().split())), list(map(int, input().split()))]
    dp = [[MAX for _ in range(n)]for _ in range(2)]
    dp[0][0] = score[0][0]
    dp[1][0] = score[1][0]
    if n == 1:
        print(max(dp[0][0],dp[1][0]))
    else:
        dp[0][1] = score[0][1] + dp[1][0]
        dp[1][1] = score[1][1] + dp[0][0]
        for j in range(2, n):
            dp[0][j] = max(dp[1][j - 1], dp[1][j - 2],dp[0][j-2]) + score[0][j]
            dp[1][j] = max(dp[0][j - 1], dp[0][j - 2],dp[1][j-2]) + score[1][j]
        print(max(max(dp[0]),max(dp[1])))