import sys
input = sys.stdin.readline
n = int(input()) #컴퓨터 수
graph =[[]for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result =0
def dfs(m):
    global result
    visited[m]= True
    for num in graph[m]:
        if not visited[num]:
            result +=1
            dfs(num)
for i in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(result)