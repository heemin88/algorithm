import sys
input = sys.stdin.readline
answer = 0 # 주어진 구역에서 승리할 수 있는지 확인
n = int(input())
graph =[]
visited=[[False for _ in range(n)] for _ in range(n)]
def dfs(x,y):
    global answer
    if (x,y) == (n-1,n-1):
        answer = 1
        visited[x][y]= True
        return
    if graph[x][y] !=0: #무한 루프 방지
        next_x = x+graph[x][y]
        next_y = y + graph[x][y]
        if 0<=next_x<n and 0<=y<n and not visited[next_x][y]: #아래
            visited[next_x][y]= True
            dfs(next_x,y)
        if 0<= next_y <n and 0<=x<n and not visited[x][next_y]: #오른쪽
            visited[x][next_y] = True
            dfs(x,next_y)
for i in range(n):
    graph.append(list(map(int,input().split())))
visited[0][0] = True
dfs(0,0)
if answer: print("HaruHaru")
else: print("Hing")

