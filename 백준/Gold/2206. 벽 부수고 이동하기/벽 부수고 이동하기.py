from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
path =[]
for i in range(n):
    path.append(list(map(int,list(sys.stdin.readline().strip()))))
visited=[[[False,False] for _ in range(m)]for _ in range(n)]
# 0은 일반 경우 ,1은 벽을 부수지 않은 애 방문 여
queue = deque([])
x = [-1,1,0,0]
y = [0,0,-1,1]
queue.append([0,0,1,0]) #(x,y,횟수,뿌순여)
result = -1
while queue:
    i,j,cnt,boo=map(int,queue.popleft())
    if i==n-1 and j==m-1:
        result = cnt
        break
    for k in range(4):#상하좌우
        boo2=boo
        dx = i+x[k]
        dy = j+y[k]
        if dx <0 or dx>=n or dy<0 or dy>=m: continue
        if path[dx][dy]==1 and boo2 ==0:
            boo2=1
            queue.append([dx, dy, cnt + 1, boo2])
        elif path[dx][dy]==0 and not visited[dx][dy][1] :
            if boo2 ==0 and visited[dx][dy][0]:
                visited[dx][dy][1] = True
                queue.append([dx, dy, cnt + 1, boo2])
            elif not visited[dx][dy][0]:
                visited[dx][dy][0] = True
                queue.append([dx, dy, cnt + 1, boo2])

print(result)