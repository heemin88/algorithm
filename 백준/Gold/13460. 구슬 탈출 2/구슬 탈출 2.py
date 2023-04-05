from collections import deque
n,m = map(int,input().split()) #가로 세로
# . (빈칸) , #(공 이동 X 벽) , 0 (구멍의 위치)
board = [list(input()) for i in range(n)]
result2 = float('inf')
visited = [[[[0] * m for i in range(n)] for j in range(m)] for k in range(n)] # 두 구슬 따로 방문처리를 위함
q = deque()
rx,ry,bx,by = 0,0,0,0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] =='B':
            bx,by = i,j
q.append([rx,ry,bx,by,1])
visited[rx][ry][bx][by]=1
def move (x,y,i,j):
    cnt=0
    while board[x+i][y+j] != '#' and board[x][y] != 'O':
        x+=i
        y+=j
        cnt +=1
    return x,y,cnt
dx =[-1,1,0,0]
dy=[0,0,-1,1]
def bfs():
    while q:
        rx,ry,bx,by,cnt = q.popleft()
        if cnt >10:
            break
        for i in range(4):
            nrx,nry,r_cnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,b_cnt = move(bx,by,dx[i],dy[i])
            if board[nbx][nby]=='O':
                continue
            if board[nrx][nry] =='O':
                print(cnt)
                return
            if nrx == nbx and nry == nby:
                if r_cnt>b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -=dx[i]
                    nby -=dy[i]
            if visited[nrx][nry][nbx][nby] == 0:
                visited[nrx][nry][nbx][nby]=1
                q.append([nrx,nry,nbx,nby,cnt+1])
    print(-1)
    return
bfs()