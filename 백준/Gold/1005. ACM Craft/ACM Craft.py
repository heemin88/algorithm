t = int(input())
def dfs(i):
    global result
    if visited[i] : return dp[i]
    time =0
    visited[i]=True
    for num in graph[i]:
        time = max(time,dfs(num))
    dp[i] = time + weight[i]
    result = max(result,dp[i])
    return dp[i]



for i in range(t):
    n,k=map(int,input().split()) #건물 개수, 건설순서 개수
    weight = []
    result = 0
    weight=list((map(int,input().split())))
    graph =[[] for _ in range(n)]
    for j in range(k):
        x,y = map(int,input().split())
        x-=1 ; y-=1
        graph[y].append(x)
    w = int(input()) #건설해야할 번호
    visited = [False for _ in range(n)]
    dp=[0 for _ in range(n)]
    dfs(w-1)
    print(result)