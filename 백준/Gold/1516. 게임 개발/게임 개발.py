import sys

input = sys.stdin.readline
n = int(input())
building = [[]]
time = [0]
dp = [0 for _ in range(n + 1)]
for i in range(n):
    temp = list(map(int, input().split()))
    time.append(temp[0])
    building.append(temp[1:-1])

def dfs(m):
    if dp[m]:
        return dp[m]
    max_cnt = 0
    for i in building[m]:
        t =dfs(i)
        max_cnt = max(t,max_cnt)
    dp[m] = max_cnt + time[m]
    return dp[m]

for x in range(1, n + 1):
    if not dp[x]:
        dfs(x)
    print(dp[x])