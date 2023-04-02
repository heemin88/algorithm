
from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
path =[]
for i in range(n):
    path.append(list(map(int,list(sys.stdin.readline().strip()))))
visited=[[False for _ in range(m)]for _ in range(n)]
queue = deque([])
x = [-1,1,0,0]
y = [0,0,-1,1]
result=[]
queue.append([0,0,1])
while queue:
    i,j,cnt=map(int,queue.popleft())
    if i==n-1 and j==m-1:
        print(cnt)
        break
    for k in range(4):#상하좌
        dx = i+x[k]
        dy = j+y[k]
        if dx <0 or dx>=n or dy<0 or dy>=m: continue
        if path[dx][dy]==1 and not visited[dx][dy]:
            visited[dx][dy]=True
            queue.append([dx,dy,cnt+1])
